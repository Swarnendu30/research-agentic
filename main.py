import os
from app.gui import launch_gui

def main():
    print("🧠 Launching Deep Research Agentic System GUI...")

    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)

    launch_gui()

if __name__ == "__main__":
    main()
