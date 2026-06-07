import json
import os
from pathlib import Path
from typing import Dict

def extract_coverage_metrics():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_dir = os.path.join(base_dir, "results")
    
    apps = ["Mifos", "MoodleStudent", "MoodleTeacher", "PHPTravels", "Parabank", "SwagLab"]
    models = ["gpt-4o-mini", "gpt-5-mini"]
    
    # Structure to hold metrics:
    # metrics[app][model] = {"verifiable": 0, "partial": 0, "unverifiable": 0, "total": 0}
    metrics: Dict[str, Dict[str, Dict[str, int]]] = {
        app: {model: {"verifiable": 0, "partial": 0, "unverifiable": 0, "total": 0} for model in models}
        for app in apps
    }
    
    for app in apps:
        for model in models:
            json_path = os.path.join(results_dir, app, model, "agent", "post-verifications.json")
            if not os.path.exists(json_path):
                print(f"File not found: {json_path}")
                continue
                
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    post_verifications = json.load(f)
                    
                    for pv in post_verifications:
                        coverage = pv.get("coverage", "unverifiable").lower()
                        if coverage in ["verifiable", "partial", "unverifiable"]:
                            metrics[app][model][coverage] += 1
                        else:
                            # Default unknown coverage types to unverifiable to ensure total accuracy
                            metrics[app][model]["unverifiable"] += 1
                        metrics[app][model]["total"] += 1
            except Exception as e:
                print(f"Error processing {json_path}: {e}")

    md_lines = [
        "# Coverage Metrics Report",
        "",
        "This report aggregates the coverage metrics (`verifiable`, `partial`, `unverifiable`) across all applications and models.",
        "",
        "| Application | Model | Verifiable | Partial | Unverifiable | Total |",
        "|-------------|-------|------------|---------|--------------|-------|"
    ]
    
    for app in apps:
        for model in models:
            data = metrics[app][model]
            md_lines.append(
                f"| {app} | {model} | {data['verifiable']} | {data['partial']} | {data['unverifiable']} | {data['total']} |"
            )
            
    md_lines.append("")
    
    out_path = os.path.join(results_dir, "verification_result.md")
    try:
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(md_lines))
        print(f"Successfully generated {out_path}")
    except Exception as e:
        print(f"Error writing markdown file: {e}")

if __name__ == "__main__":
    extract_coverage_metrics()
