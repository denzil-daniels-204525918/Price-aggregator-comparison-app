## Reflection

The available options—such as Basic Kanban, Automated Kanban, and Bug Triage—each cater to different workflows. Selecting the best one required evaluating factors like automation, ease of use, and alignment with Agile methodologies.

* Balancing simplicity and automation was a key challenge in selecting a GitHub project template. The Automated Kanban template offered auto-moving issues, which improved workflow efficiency, but it still required fine-tuning to align with sprint-based development. Customization was necessary to add key columns such as Testing and Blocked, ensuring that tasks followed Agile principles while maintaining flexibility in managing work.
* Implementing Work-in-Progress (WIP) limits within GitHub’s Kanban system also posed challenges. Unlike Jira, which allows configurable WIP limits per column, GitHub lacks a built-in enforcement mechanism, making it necessary to track WIP manually. 
* Despite these challenges, integrating GitHub Issues with the Kanban board was seamless. User stories could be linked directly to tasks, streamlining the tracking process.

## Comparison

| Feature         | GitHub Projects (Kanban)           | Trello                                  | Jira                                       |
|----------------|-----------------------------------|-----------------------------------------|--------------------------------------------|
| **Customization** | Moderate (predefined templates, customizable columns) | High (drag-and-drop, custom fields) | Advanced (fully customizable workflows) |
| **Automation** | Basic (auto-moving issues in Automated Kanban) | Moderate (rules & automation with Power-Ups) | Advanced (custom scripts & workflow automation) |
| **Issue Tracking** | Integrated with GitHub Issues | Requires Power-Ups or third-party tools | Built-in issue tracking |
| **WIP Limits** | Manual tracking required | Can use labels for tracking | Built-in enforcement |
| **Collaboration** | Good (works well with GitHub repositories) | Excellent (intuitive UI for teams) | Enterprise-level (permissions, role management) |
| **Best For** | Developers using GitHub | General project management | Large Agile teams & enterprises |

## Conclusion
While Jira offers the most robust Agile features, it is complex and may be overkill for smaller teams. Trello provides flexibility but lacks deep issue tracking. GitHub Projects is the best choice for development teams working within GitHub, as it directly integrates with Issues and repositories, streamlining workflows. Despite some customisation challenges, it effectively supports Agile sprints, task tracking, and collaboration.
