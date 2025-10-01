#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

function info(msg) {
    console.log(`[INFO] ${msg}`);
}

function copyFileOrDir(src, dest) {
    info(`Updating ${src} to ${dest}`);

    if (fs.statSync(src).isDirectory()) {
        // Copy directory recursively
        if (!fs.existsSync(dest)) {
            fs.mkdirSync(dest, { recursive: true });
        }
        const entries = fs.readdirSync(src);
        for (const entry of entries) {
            copyFileOrDir(path.join(src, entry), path.join(dest, entry));
        }
    } else {
        // Copy file
        const destDir = path.dirname(dest);
        if (!fs.existsSync(destDir)) {
            fs.mkdirSync(destDir, { recursive: true });
        }
        fs.copyFileSync(src, dest);
    }
}

function updatePrompts(dryRun = false) {
    // Track files that are created/copied
    const addedFiles = [];

    // Get the project root (where package.json is located)
    const projectRoot = path.dirname(__dirname);
    const assetsDir = path.join(projectRoot, 'assets');

    if (!fs.existsSync(assetsDir)) {
        console.error(`Error: Assets directory not found at ${assetsDir}`);
        process.exit(1);
    }

    // Copy daksh-prompts to .daksh
    const promptsSource = path.join(assetsDir, 'daksh-prompts');
    const promptsDest = '.daksh';

    if (!dryRun) {
        // Remove existing .daksh folder before copying
        if (fs.existsSync(promptsDest)) {
            info('Removing existing .daksh folder');
            fs.rmSync(promptsDest, { recursive: true, force: true });
        }

        // Copy each subdirectory individually to track them
        if (fs.existsSync(promptsSource)) {
            if (!fs.existsSync(promptsDest)) {
                fs.mkdirSync(promptsDest, { recursive: true });
            }
            const entries = fs.readdirSync(promptsSource);
            for (const entry of entries) {
                const srcPath = path.join(promptsSource, entry);
                const destPath = path.join(promptsDest, entry);
                copyFileOrDir(srcPath, destPath);
                addedFiles.push(destPath);
            }
        }
    } else {
        info(`Would remove existing ${promptsDest} and copy ${promptsSource} to ${promptsDest}`);
    }

    // Update .vscode/settings.json
    const vscodePath = '.vscode/settings.json';
    let settings = {};

    if (fs.existsSync(vscodePath)) {
        try {
            settings = JSON.parse(fs.readFileSync(vscodePath, 'utf8'));
        } catch (e) {
            info('Warning: Could not parse existing .vscode/settings.json');
        }
    }

    if (!settings['chat.modeFilesLocations']) {
        settings['chat.modeFilesLocations'] = {};
    }
    settings['chat.modeFilesLocations']['.daksh/prompts/**/'] = true;

    if (!dryRun) {
        if (!fs.existsSync('.vscode')) {
            fs.mkdirSync('.vscode', { recursive: true });
        }
        fs.writeFileSync(vscodePath, JSON.stringify(settings, null, 2));
        addedFiles.push(vscodePath);
    } else {
        info(`Would update ${vscodePath}`);
    }

     // Update .vscode/mcp.json
    const mcpPath = '.vscode/mcp.json';
    let mcpConfig = {
        servers: {}
    };

    if (fs.existsSync(mcpPath)) {
        try {
            mcpConfig = JSON.parse(fs.readFileSync(mcpPath, 'utf8'));
        } catch (e) {
            info('Warning: Could not parse existing .vscode/mcp.json');
        }
    }

    // Ensure servers object exists
    if (!mcpConfig.servers) {
        mcpConfig.servers = {};
    }

    // Add common MCP servers if they don't exist
    if (!mcpConfig.servers['@modelcontextprotocol/server-filesystem']) {
        mcpConfig.servers['@modelcontextprotocol/server-filesystem'] = {
            command: 'npx',
            args: ['-y', '@modelcontextprotocol/server-filesystem', process.cwd()]
        };
    }

    if (!dryRun) {
        fs.writeFileSync(mcpPath, JSON.stringify(mcpConfig, null, 2));
        addedFiles.push(mcpPath);
    } else {
        info(`Would update ${mcpPath}`);
    }


    // Handle copilot-instructions.md backup and copy
    const copilotInstructions = '.github/copilot-instructions.md';
    if (fs.existsSync(copilotInstructions) && !dryRun) {
        const readline = require('readline');
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

        rl.question('Found an existing .github/copilot-instructions.md should we back it up? [y/N]: ', (answer) => {
            if (answer.toLowerCase() === 'y') {
                const timestamp = new Date().toISOString().replace(/[:.]/g, '').replace('T', '').slice(0, 14);
                const backup = `.github/copilot-instructions.md.bak.${timestamp}`;
                info(`Backing up existing .github/copilot-instructions.md to ${backup}`);
                fs.copyFileSync(copilotInstructions, backup);
                addedFiles.push(backup);
            } else {
                info('Skipping backup');
            }
            rl.close();
            continueSetup();
        });
        return;
    }

    continueSetup();

    function continueSetup() {
        if (!dryRun) {
            // Ensure .github directory exists
            if (!fs.existsSync('.github')) {
                fs.mkdirSync('.github', { recursive: true });
            }

            // Copy files from assets
            fs.copyFileSync(path.join(assetsDir, 'copilot-instructions.md'), copilotInstructions);
            addedFiles.push(copilotInstructions);

            fs.copyFileSync(path.join(assetsDir, 'mkdocs.yml'), 'mkdocs.yml');
            addedFiles.push('mkdocs.yml');

            // Copy CSS and overrides
            if (!fs.existsSync('docs/overrides')) {
                fs.mkdirSync('docs/overrides', { recursive: true });
            }
            fs.copyFileSync(path.join(assetsDir, 'extra.css'), 'docs/overrides/extra.css');
            addedFiles.push('docs/overrides/extra.css');

            copyFileOrDir(path.join(assetsDir, 'overrides'), './overrides');
            addedFiles.push('./overrides');

            // Copy index.md if it doesn't exist
            if (!fs.existsSync('docs/index.md')) {
                fs.copyFileSync(path.join(assetsDir, 'index.md'), 'docs/index.md');
                addedFiles.push('docs/index.md');
            }

            // Display summary of added files
            console.log('\n📁 Files added to current working directory:');
            addedFiles.forEach(file => {
                console.log(`   ✓ ${file}`);
            });
            console.log(`\nTotal: ${addedFiles.length} files/directories added or updated\n`);
        } else {
            info('Dry run complete - no files were modified');
        }
    }
}

function showHelp() {
    console.log(`
daksh - Documentation & Artifact Knowledge Synchronization Hub

Usage: daksh <command> [options]

Commands:
  update-prompts [--dry-run]    Update project with daksh prompts and configuration

Options:
  --dry-run                     Show what would be done without making changes
  --help, -h                    Show this help message

Examples:
  daksh update-prompts          Update project with latest prompts
  daksh update-prompts --dry-run Preview changes without applying them
`);
}

// Parse command line arguments
const args = process.argv.slice(2);

if (args.length === 0 || args.includes('--help') || args.includes('-h')) {
    showHelp();
    process.exit(0);
}

const command = args[0];
const dryRun = args.includes('--dry-run');

switch (command) {
    case 'update-prompts':
        updatePrompts(dryRun);
        break;
    default:
        console.error(`Unknown command: ${command}`);
        showHelp();
        process.exit(1);
}