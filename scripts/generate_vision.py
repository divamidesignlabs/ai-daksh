import os
import re
from pathlib import Path
from collections import defaultdict

def extract_key_points(markdown_files):
    """
    Extract key information from converted markdown files to build a vision document.
    """
    data = {
        "problems": [],
        "features": [],
        "user_types": set(),
        "requirements": [],
        "goals": [],
        "scope": {"in": [], "out": []},
        "differentiators": []
    }
    
    # Keywords to look for in the files
    keywords = {
        "problems": ["problem", "challenge", "pain point", "issue", "difficulty"],
        "features": ["feature", "capability", "function", "component"],
        "users": ["user", "persona", "role", "stakeholder", "client"],
        "goals": ["goal", "objective", "success", "metric", "KPI", "outcome"],
        "scope": ["scope", "boundary", "limit", "constraint"],
        "differentiators": ["differentiator", "unique", "advantage", "competitive"]
    }
    
    for file_path in markdown_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract user stories
            user_stories = re.findall(r"As an? ([^,]+)", content, re.IGNORECASE)
            user_stories.extend(re.findall(r"As a ([^,]+)", content, re.IGNORECASE))
            
            for user in user_stories:
                if len(user.split()) <= 3:  # Avoid capturing entire sentences
                    data["user_types"].add(user.strip())
            
            # Extract requirements as potential features
            req_blocks = re.findall(r"(?:REQ|TASK|MEET)-\d+[^\n]+", content)
            for req in req_blocks:
                clean_req = re.sub(r"(?:REQ|TASK|MEET)-\d+\s*", "", req).strip()
                if clean_req and len(clean_req) > 10:  # Avoid short fragments
                    data["requirements"].append(clean_req)
            
            # Scan for sentences containing keywords
            paragraphs = content.split('\n\n')
            for para in paragraphs:
                lines = para.split('\n')
                for line in lines:
                    line = line.strip()
                    if not line or line.startswith('#') or len(line) < 15:
                        continue
                        
                    # Check for problem statements
                    if any(keyword in line.lower() for keyword in keywords["problems"]):
                        if "not" not in line.lower() and "shouldn't" not in line.lower():
                            data["problems"].append(line)
                    
                    # Check for features
                    if any(keyword in line.lower() for keyword in keywords["features"]):
                        if line not in data["features"] and len(line) < 200:
                            data["features"].append(line)
                    
                    # Check for goals/metrics
                    if any(keyword in line.lower() for keyword in keywords["goals"]):
                        if "%" in line or "increase" in line.lower() or "reduce" in line.lower():
                            data["goals"].append(line)
                    
                    # Check for scope
                    if any(keyword in line.lower() for keyword in keywords["scope"]):
                        if "not" in line.lower() or "shouldn't" in line.lower():
                            data["scope"]["out"].append(line)
                        else:
                            data["scope"]["in"].append(line)
                    
                    # Check for differentiators
                    if any(keyword in line.lower() for keyword in keywords["differentiators"]):
                        data["differentiators"].append(line)
        
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    # Deduplicate and clean up data
    for key in data:
        if isinstance(data[key], list):
            data[key] = list(set(data[key]))
        elif isinstance(data[key], dict):
            for subkey in data[key]:
                data[key][subkey] = list(set(data[key][subkey]))
    
    return data

def generate_vision_statement(data):
    """Generate a vision statement from the extracted data"""
    features = data["features"][:3]  # Take top 3 features
    user_types = list(data["user_types"])[:2]  # Take top 2 user types
    
    if features and user_types:
        vision = f"To create an intelligent, context-aware system that helps {' and '.join(user_types)} "
        vision += f"manage {', '.join(f for f in features if len(f) < 50)[:100]} "
        vision += "using automation, AI suggestions, and structured workflows."
        return vision
    else:
        return "To create an intelligent, context-aware task and meeting management system that helps enterprise users work more efficiently through automation, contextual awareness, and structured workflows."

def create_vision_md(data, output_path):
    """Create the vision.md file with the extracted information"""
    
    vision_statement = generate_vision_statement(data)
    
    # Format user types/personas
    user_personas = "\n\n".join([f"- **{user.title()}**: Interacts with the system to manage tasks, meetings, and related workflows." 
                               for user in list(data["user_types"])[:5]])
    
    # Format problem statements
    problems = "\n\n".join([f"- {problem}" for problem in data["problems"][:5]])
    
    # Format features
    features = "\n\n".join([f"- {feature}" for feature in data["features"][:8]])
    
    # Format goals
    goals = "\n\n".join([f"- {goal}" for goal in data["goals"][:5]])
    
    # Format scope
    in_scope = "\n\n".join([f"- ✅ {item}" for item in data["scope"]["in"][:5]])
    out_scope = "\n\n".join([f"- ❌ {item}" for item in data["scope"]["out"][:5]])
    
    # Format differentiators
    differentiators = "\n\n".join([f"- {diff}" for diff in data["differentiators"][:5]])
    
    # Add requirements as differentiators if we don't have enough
    if len(data["differentiators"]) < 3:
        for req in data["requirements"][:3]:
            if "uniquely" in req.lower() or "advanced" in req.lower():
                differentiators += f"\n\n- {req}"
    
    # Generate timeline (placeholder)
    timeline = """- **Q1 2026**: Core task and meeting management capabilities
    
- **Q2 2026**: Calendar integration & recurrence features
    
- **Q3 2026**: AI-generated suggestions and automation
    
- **Q4 2026**: Integration with external systems and analytics"""
    
    vision_content = f"""# Product Vision – Task and Meeting Management System

## 1. Vision Statement

{vision_statement}

## 2. Target Users / Personas

{user_personas or "- **Task Manager**: Creates and assigns tasks, monitors completion.\n\n- **Meeting Organizer**: Schedules and tracks meetings, records outcomes.\n\n- **Team Member**: Participates in tasks and meetings, updates status."}

## 3. Problem Statements

{problems or "- Users lack centralized visibility of their tasks.\n\n- No way to manage follow-ups intelligently.\n\n- Meetings are logged inconsistently and lack structured outcomes."}

## 4. Key Capabilities / Features

{features or "- Smart Assistant for quick task and meeting creation\n\n- AI-based content suggestions for meetings and tasks\n\n- Dashboard with real-time task metrics and visual indicators\n\n- Role-based access control for tasks, meetings, and entities"}

## 5. Business Goals & Success Metrics

{goals or "- 80% task creation via Smart Assistant within 3 months\n\n- <5% overdue critical tasks after implementation\n\n- 90% accuracy in AI-generated suggestions adoption\n\n- 100% meeting linkage to relevant entities"}

## 6. Scope & Boundaries

{in_scope or "- ✅ Task creation, assignment, and tracking\n\n- ✅ Meeting scheduling, recording, and follow-up\n\n- ✅ Dashboard and reporting\n\n- ✅ Integration with calendar systems"}

{out_scope or "- ❌ Billing and invoicing features\n\n- ❌ Project management capabilities\n\n- ❌ Customer relationship management\n\n- ❌ Document management system"}

## 7. Timeline / Milestones

{timeline}

## 8. Strategic Differentiators

{differentiators or "- AI-assisted workflows embedded into daily task/meeting UX\n\n- Context-aware task creation from system entities\n\n- Lightweight yet structured compliance through business rules"}
"""

    # Write to the output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(vision_content)
    
    print(f"Vision.md created successfully at {output_path}")

def main():
    # Paths
    converted_dir = Path("/Users/rahul/Desktop/Daksh_Divami/daksh/docs/converted")
    output_path = Path("/Users/rahul/Desktop/Daksh_Divami/daksh/docs/specifications/business/vision.md")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_path.parent, exist_ok=True)
    
    # Find all markdown files
    markdown_files = []
    for root, _, files in os.walk(converted_dir):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    
    print(f"Found {len(markdown_files)} markdown files to process")
    
    # Extract data from markdown files
    data = extract_key_points(markdown_files)
    
    # Create vision.md
    create_vision_md(data, output_path)
    
    print("Vision document generation complete!")

if __name__ == "__main__":
    main()