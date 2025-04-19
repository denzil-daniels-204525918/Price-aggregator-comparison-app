One of the key challenges encountered during the modeling phase was determining the appropriate level of granularity for states 
and actions. Striking a balance between detail and readability proved essential. Diagrams that were overly detailed became 
difficult to interpret, especially for stakeholders who were less familiar with UML, while oversimplified diagrams risked 
missing critical behaviors. For instance, in modeling the Price Alert object, I chose to abstract technical distinctions 
like notification types (email, push, etc.) and instead focused on broader state transitions such as Subscribed to Notified, 
to maintain clarity without losing essential information.

Another challenge involved aligning state and activity diagrams with Agile user stories. While user stories are user-centered 
and narrative-driven, UML diagrams are system-focused and require more technical interpretation. Bridging this gap required 
careful mapping of system behaviors to specific user intentions. For example, the Saved List diagram was crafted specifically 
to reflect the user story: "As a user, I want to save my favorite products." This helped define the necessary actions and 
transitions such as saving, removing, and sharing list items.

It was also important to understand the difference between state diagrams and activity diagrams to effectively use both in my 
system modeling. State diagrams describe the lifecycle of a specific object by outlining its states, transitions, and triggering 
events or conditions. In contrast, activity diagrams depict the overall workflow or process, including user actions, decision 
points, and parallel operations. While state diagrams aligned closely with functional requirements and object-specific behavior, 
activity diagrams were more effective in mapping workflows related to user stories and sprint tasks. For instance, a state diagram 
clearly illustrated the stages of a Retailer Dashboard Access request, whereas an activity diagram helped visualise how a user 
builds and shares a grocery list step-by-step. Using both diagram types together provided a holistic view of system behavior 
and user interaction, supporting Agile principles such as continuous delivery, transparency, and adaptability.