#!/usr/bin/env python3
import os
import csv
import re
import argparse

def slugify(title):
    # lower, replace non-alnum with -, strip leading/trailing -
    s = title.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s

def generate(tracker_path, problem_id):
    with open(tracker_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['ID'].strip() != problem_id:
                continue

            topic = row['Topic'].strip()
            title = row['Title'].strip()
            revisit = row.get('Revisit', '').strip()

            slug = slugify(title)
            folder = topic
            os.makedirs(folder, exist_ok=True)

            filename = f"{problem_id}-{slug}.py"
            fullpath = os.path.join(folder, filename)

            if os.path.exists(fullpath):
                print(f"[skipped] {fullpath} already exists")
                return

            link = f"https://leetcode.com/problems/{slug}/"
            tpl = f'''"""
LeetCode {problem_id}: {title}
{link}

📝 Summary:

🧠 Thought Process:

✅ Solution Approach:

🐞 Mistakes & Gotchas:

🎓 What I Learned:

🔁 Revisit: {revisit}
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # TODO: implement
        pass
'''

            with open(fullpath, 'w') as out:
                out.write(tpl)
            print(f"[created] {fullpath}")
            return

    print(f"[error] ID {problem_id} not found in {tracker_path}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Generate a LeetCode template from tracker.csv")
    p.add_argument("id", nargs="?", help="Problem ID (e.g. 228)")
    p.add_argument("--tracker", default="tracker.csv",
                   help="Path to your tracker.csv")
    
    args = p.parse_args()
    if args.id is None:
         print("❗ Please provide a Problem ID (e.g. 228)")
         exit(1)
         
    generate(args.tracker, args.id)
