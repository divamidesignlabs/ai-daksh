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
    const settingsSource = path.join(assetsDir, 'json-files', 'settings.json');
    
    if (!dryRun) {
        if (!fs.existsSync('.vscode')) {
            fs.mkdirSync('.vscode', { recursive: true });
        }
        
        let settings = {};
        
        // Read existing settings if they exist
        if (fs.existsSync(vscodePath)) {
            try {
                settings = JSON.parse(fs.readFileSync(vscodePath, 'utf8'));
            } catch (e) {
                info('Warning: Could not parse existing .vscode/settings.json');
            }
        }
        
        // Read template settings from assets
        if (fs.existsSync(settingsSource)) {
            try {
                const templateSettings = JSON.parse(fs.readFileSync(settingsSource, 'utf8'));
                // Merge template settings with existing settings
                settings = { ...settings, ...templateSettings };
            } catch (e) {
                info('Warning: Could not parse template settings.json');
            }
        }
        
        fs.writeFileSync(vscodePath, JSON.stringify(settings, null, 2));
        addedFiles.push(vscodePath);
    } else {
        info(`Would update ${vscodePath} using template from ${settingsSource}`);
    }

     // Update .vscode/mcp.json
    const mcpPath = '.vscode/mcp.json';
    const mcpSource = path.join(assetsDir, 'json-files', 'mcp.json');
    
    if (!dryRun) {
        let mcpConfig = { servers: {} };
        
        // Read existing mcp.json if it exists
        if (fs.existsSync(mcpPath)) {
            try {
                mcpConfig = JSON.parse(fs.readFileSync(mcpPath, 'utf8'));
            } catch (e) {
                info('Warning: Could not parse existing .vscode/mcp.json');
            }
        }
        
        // Read template mcp.json from assets
        if (fs.existsSync(mcpSource)) {
            try {
                const templateMcp = JSON.parse(fs.readFileSync(mcpSource, 'utf8'));
                // Merge template with existing config, preserving existing servers
                if (!mcpConfig.servers) mcpConfig.servers = {};
                mcpConfig.servers = { ...mcpConfig.servers, ...templateMcp.servers };
            } catch (e) {
                info('Warning: Could not parse template mcp.json');
            }
        }
        
        fs.writeFileSync(mcpPath, JSON.stringify(mcpConfig, null, 2));
        addedFiles.push(mcpPath);
    } else {
        info(`Would update ${mcpPath} using template from ${mcpSource}`);
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

            // fs.copyFileSync(path.join(assetsDir, 'mcp_deps.txt'), 'mcp_deps.txt');
            // addedFiles.push('mcp_deps.txt');

            // Copy CSS and overrides
            if (!fs.existsSync('docs/overrides')) {
                fs.mkdirSync('docs/overrides', { recursive: true });
            }
            fs.copyFileSync(path.join(assetsDir, 'extra.css'), 'docs/overrides/extra.css');
            addedFiles.push('docs/overrides/extra.css');

            copyFileOrDir(path.join(assetsDir, 'overrides'), './overrides');
            addedFiles.push('./overrides');

            // Copy fastMcp folder
            // copyFileOrDir(path.join(assetsDir, 'fastMcp'), './fastMcp');
            // addedFiles.push('./fastMcp');

            // Copy index.md if it doesn't exist
            if (!fs.existsSync('docs/index.md')) {
                fs.copyFileSync(path.join(assetsDir, 'index.md'), 'docs/index.md');
                addedFiles.push('docs/index.md');
            }

            // Copy mkdocs helper files if present in assets
            ['mkdocs_deps.txt', 'run-mkdocs.sh'].forEach(f => {
                const srcF = path.join(assetsDir, f);
                if (fs.existsSync(srcF)) {
                    fs.copyFileSync(srcF, f);
                    if (f.endsWith('.sh')) {
                        try { fs.chmodSync(f, 0o755); } catch (e) { info(`Could not chmod ${f}: ${e.message}`); }
                    }
                    addedFiles.push(f);
                }
            });

            // Create or update .vscode/tasks.json
            const tasksPath = '.vscode/tasks.json';
            const tasksSource = path.join(assetsDir, 'json-files', 'tasks.json');
            
            let tasksData = { version: '2.0.0', tasks: [] };
            
            // Read existing tasks.json if it exists
            if (fs.existsSync(tasksPath)) {
                try {
                    tasksData = JSON.parse(fs.readFileSync(tasksPath, 'utf8'));
                } catch (e) {
                    info('Warning: Could not parse existing tasks.json; using template');
                }
            }
            
            // Read template tasks.json from assets
            if (fs.existsSync(tasksSource)) {
                try {
                    const templateTasks = JSON.parse(fs.readFileSync(tasksSource, 'utf8'));
                    // Use template tasks, but preserve version and merge with existing if needed
                    tasksData = { ...tasksData, ...templateTasks };
                } catch (e) {
                    info('Warning: Could not parse template tasks.json');
                }
            }
            
            if (!fs.existsSync('.vscode')) fs.mkdirSync('.vscode', { recursive: true });
            fs.writeFileSync(tasksPath, JSON.stringify(tasksData, null, 2));
            addedFiles.push(tasksPath);

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

// New command: research-prompts
// Mirror of update-prompts but ONLY copies the templates folder from assets/daksh-prompts
// and adjusts VS Code settings to reference templates instead of prompts.
function updateResearchPrompts(dryRun = false) {
    const addedFiles = [];
    const projectRoot = path.dirname(__dirname);
    const assetsDir = path.join(projectRoot, 'assets');
    const promptsSource = path.join(assetsDir, 'daksh-prompts');
    const templatesSource = path.join(promptsSource, 'templates');
    const dakshDir = '.daksh';

    if (!fs.existsSync(assetsDir)) {
        console.error(`Error: Assets directory not found at ${assetsDir}`);
        process.exit(1);
    }
    if (!fs.existsSync(promptsSource)) {
        console.error(`Error: daksh-prompts directory not found at ${promptsSource}`);
        process.exit(1);
    }
    if (!fs.existsSync(templatesSource)) {
        console.error(`Error: templates directory not found at ${templatesSource}`);
        process.exit(1);
    }

    // Reset .daksh and copy only templates
    if (!dryRun) {
        if (fs.existsSync(dakshDir)) {
            info('Removing existing .daksh folder');
            fs.rmSync(dakshDir, { recursive: true, force: true });
        }
        fs.mkdirSync(dakshDir, { recursive: true });
        copyFileOrDir(templatesSource, path.join(dakshDir, 'templates'));
        addedFiles.push(path.join(dakshDir, 'templates'));
    } else {
        info(`Would recreate ${dakshDir} and copy only ${templatesSource} -> ${dakshDir}/templates`);
    }

    // Update .vscode/settings.json (same merge logic as update-prompts but swap prompts path with templates path)
    const vscodePath = '.vscode/settings.json';
    const settingsSource = path.join(assetsDir, 'json-files', 'settings.json');
    let settings = {};
    if (fs.existsSync(vscodePath)) {
        try { settings = JSON.parse(fs.readFileSync(vscodePath, 'utf8')); } catch { info('Warning: Could not parse existing .vscode/settings.json'); }
    }
    if (fs.existsSync(settingsSource)) {
        try {
            const templateSettings = JSON.parse(fs.readFileSync(settingsSource, 'utf8'));
            settings = { ...settings, ...templateSettings };
        } catch { info('Warning: Could not parse template settings.json'); }
    }
    // Adjust chat.modeFilesLocations: remove any prompts glob, add templates glob
    if (!settings['chat.modeFilesLocations']) settings['chat.modeFilesLocations'] = {};
    for (const key of Object.keys(settings['chat.modeFilesLocations'])) {
        if (key.includes('.daksh/prompts')) delete settings['chat.modeFilesLocations'][key];
    }
    settings['chat.modeFilesLocations']['.daksh/templates/**/'] = true;
    if (!dryRun) {
        if (!fs.existsSync('.vscode')) fs.mkdirSync('.vscode', { recursive: true });
        fs.writeFileSync(vscodePath, JSON.stringify(settings, null, 2));
        addedFiles.push(vscodePath);
    } else {
        info(`Would write merged settings with templates glob to ${vscodePath}`);
    }

    // Update .vscode/mcp.json (reuse merge logic from update-prompts)
    const mcpPath = '.vscode/mcp.json';
    const mcpSource = path.join(assetsDir, 'json-files', 'mcp.json');
    if (!dryRun) {
        let mcpConfig = { servers: {} };
        if (fs.existsSync(mcpPath)) {
            try { mcpConfig = JSON.parse(fs.readFileSync(mcpPath, 'utf8')); } catch { info('Warning: Could not parse existing .vscode/mcp.json'); }
        }
        if (fs.existsSync(mcpSource)) {
            try {
                const templateMcp = JSON.parse(fs.readFileSync(mcpSource, 'utf8'));
                if (!mcpConfig.servers) mcpConfig.servers = {};
                mcpConfig.servers = { ...mcpConfig.servers, ...templateMcp.servers };
            } catch { info('Warning: Could not parse template mcp.json'); }
        }
        if (!fs.existsSync('.vscode')) fs.mkdirSync('.vscode', { recursive: true });
        fs.writeFileSync(mcpPath, JSON.stringify(mcpConfig, null, 2));
        addedFiles.push(mcpPath);
    } else {
        info(`Would merge template ${mcpSource} into ${mcpPath}`);
    }

    // Handle copilot-instructions backup & copying (same as update-prompts)
    const copilotInstructions = '.github/copilot-instructions.md';
    const proceed = () => continueSetup();
    if (fs.existsSync(copilotInstructions) && !dryRun) {
        const readline = require('readline');
        const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
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
            proceed();
        });
        return; // wait for async question
    }
    continueSetup();

    function continueSetup() {
        if (!dryRun) {
            if (!fs.existsSync('.github')) fs.mkdirSync('.github', { recursive: true });
            fs.copyFileSync(path.join(assetsDir, 'copilot-instructions.md'), copilotInstructions);
            addedFiles.push(copilotInstructions);
            fs.copyFileSync(path.join(assetsDir, 'mkdocs.yml'), 'mkdocs.yml');
            addedFiles.push('mkdocs.yml');
            if (!fs.existsSync('docs/overrides')) fs.mkdirSync('docs/overrides', { recursive: true });
            fs.copyFileSync(path.join(assetsDir, 'extra.css'), 'docs/overrides/extra.css');
            addedFiles.push('docs/overrides/extra.css');
            copyFileOrDir(path.join(assetsDir, 'overrides'), './overrides');
            addedFiles.push('./overrides');
            if (!fs.existsSync('docs/index.md')) {
                fs.copyFileSync(path.join(assetsDir, 'index.md'), 'docs/index.md');
                addedFiles.push('docs/index.md');
            }
            ['mkdocs_deps.txt', 'run-mkdocs.sh'].forEach(f => {
                const srcF = path.join(assetsDir, f);
                if (fs.existsSync(srcF)) {
                    fs.copyFileSync(srcF, f);
                    if (f.endsWith('.sh')) { try { fs.chmodSync(f, 0o755); } catch (e) { info(`Could not chmod ${f}: ${e.message}`); } }
                    addedFiles.push(f);
                }
            });
            // tasks.json merge
            const tasksPath = '.vscode/tasks.json';
            const tasksSource = path.join(assetsDir, 'json-files', 'tasks.json');
            let tasksData = { version: '2.0.0', tasks: [] };
            if (fs.existsSync(tasksPath)) { try { tasksData = JSON.parse(fs.readFileSync(tasksPath, 'utf8')); } catch { info('Warning: Could not parse existing tasks.json; using template'); } }
            if (fs.existsSync(tasksSource)) { try { const templateTasks = JSON.parse(fs.readFileSync(tasksSource, 'utf8')); tasksData = { ...tasksData, ...templateTasks }; } catch { info('Warning: Could not parse template tasks.json'); } }
            if (!fs.existsSync('.vscode')) fs.mkdirSync('.vscode', { recursive: true });
            fs.writeFileSync(tasksPath, JSON.stringify(tasksData, null, 2));
            addedFiles.push(tasksPath);
            console.log('\n📁 Files added to current working directory (research-prompts):');
            addedFiles.forEach(f => console.log(`   ✓ ${f}`));
            console.log(`\nTotal: ${addedFiles.length} files/directories added or updated\n`);
        } else {
            info('Dry run complete - no files were modified (research-prompts)');
        }
    }
}



function showHelp() {
    console.log(`
daksh - Documentation & Artifact Knowledge Synchronization Hub

Usage: daksh <command> [options]

Commands:
  update-prompts [--dry-run]    Update project with daksh prompts and configuration
    research-prompts [--dry-run]  Update project but only include templates (not prompts) into .daksh

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
    case 'research-prompts':
        updateResearchPrompts(dryRun);
        break;
    default:
        console.error(`Unknown command: ${command}`);
        showHelp();
        process.exit(1);
}