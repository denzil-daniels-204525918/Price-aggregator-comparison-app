## Reflection on Domain Modeling and Class Diagram Design

A challenge faced in designing the model was deciding how to apply the classes when modeling objects. 
With the absence of conventional objects, I had to focus on more conceptual objects like `SavedList`, `PriceAlert`, and `Promotion`, 
which are user-centric and align more with the core value proposition of the system.

Another challenge was accurately defining **relationships** among entities while maintaining simplicity and clarity. 
It was tempting to over-engineer certain associations, such as between `User` and `Product`, especially when considering 
potential features like user tracking, wish listing, and browsing history. I had to balance between what could be useful 
for future development versus what was essential to the current scope of the system.

Furthermore, defining **methods or class responsibilities** was occasionally ambiguous. Since most of our application’s 
behavior is either user-initiated (e.g., sharing a list) or automated (e.g., sending a price drop alert), encapsulating 
that logic within class definitions felt forced at times.This is resolved by focusing on high-level responsibilities
each class should manage, without diving too deep.

### Alignment with Previous Assignments

The class diagram is strongly informed by the earlier assignments, using critical functionality such as user account management, 
price alert subscriptions, and retailer product management. Each of these features maps directly to one or more classes in the 
domain model. For instance, `PriceAlert` and `SavedList` originate directly from those requirements. The **use cases from Assignment 5** also provided clear boundaries for class responsibilities. For example, the user goal 
of “subscribing to a price alert” helped justify a dedicated `PriceAlert` class with a tight coupling to the `User` and `Product` 
classes. Similarly, the `Retailer` class was validated by the use case where a retailer must manage and update their product listings. The **state and activity diagrams from Assignment 8** influenced the methods and states considered in the class definitions. 
For instance, the state transitions for `Retailer Dashboard Access` helped us understand that access control is a policy issue, 
not just a relationship, and should be reflected in class logic or permissions. These behavioral models reinforced decisions such 
as whether certain attributes should be booleans (e.g., `isActive`) or full-blown states (e.g., `status = ['active', 'pending', 'revoked']`).

### Trade-offs Made

Several trade-offs were made during the modeling process. One of the main decisions was **avoiding unnecessary inheritance**. 
While it was technically possible to create a superclass for `User` and `Retailer`, the feeling was that this would add more 
complexity than value given the relatively small overlap in attributes and responsibilities. 
Instead, opting for composition and associations. Additionally, simplifying certain relationships that might later benefit from more granularity. For instance, the connection between 
`SavedList` and `Product` was modeled as a many-to-many association without considering list categories or timestamps for when 
items were added. These were consciously excluded to keep the diagram readable and focused on the most essential relationships. Another trade-off was **method visibility and detail**. Highlighting classes that were critical to capturing system behavior at 
a high level keeps the diagram maintainable and digestible for stakeholders who are more interested in functionality 
than low-level implementation.

### 4. Lessons Learned

This exercise deepened my understanding of object-oriented design principles. The importance of assigning clear responsibilities to each class and minimising the interdependence between them 
stood out as a key takeaway. I've also gained an understanding for how early planning artifacts like user stories and requirements inform later design decisions. 
Having a well-articulated functional foundation meant that I wasn't starting from scratch when modeling our domain; 
I'm simply refining and structuring what was already implicit in earlier work.

In conclusion, designing the domain model and class diagram is a complex but rewarding process that brings clarity to my 
system's structure and paved the way for future development and scalability.
