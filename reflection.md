# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

- Answer: I designed 4 classes: Task,Pet,Owner,and Scheduler. Each with their separate responsibility and subsections/child sections that allowed for a streamlined process.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

- Answer: Yes, I was originally planning on having the Scheduler's sort by time and detect_conflicts method work with no arguments, but I later decided to change them to accept the tasks list as an input. I did this because after testing I noticed it would provide more flexibility and would overall be much more easier to test.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

-  Answer: What i've noticed is that the scheduler considers time as the main constraint - tasks are sorted by their time attributes. I chose time as the delegated constraint because these tasks are time sensitive and are detrimental in the context of animal/petcare. 


**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

- Answer: The conflict detection set up only checks for the exact time matches, not the overlapping durations which I understand may be a prevalent feature in real world/day-to-day activities. However, if we assign ourselves within the concept of a simple AI project, it's not too bad.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

- Answer: I used GitHub Copilot to help draft and brainstorm the design and generate a layout of useful code. I would then go in and nitpick any extra code pieces, because my initial attempt of testing the code went abrupt very quickly as my "fixes" were ironically causing more errors. 



**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

- Answer: Jason Wodicka mentions how you should stray away from vagueness and sometimes during these run attempts I could tell that sometimes my prompts were lacking in specificity. Though after some time debugging I was able to run the test and confirm that all my tests passed.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

- Answer: I tested things like task completion where is_complete is set to true, adding tasks to pets increases the task count and sorting returns in order, recurring tasks, and of course conflict detection to flag duplicates. I find that these tests were important because without them the app would only do the bare minimum - which was run. But it would just bean "empty run" - not useful in day-to-day implementation. 

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

- Answer: I would have to say I am considerably confident because even though it took me a great deal of time, all of my tests (6 total) passed in the end with flying colors. If I had more time I would like to try out really niche edge cases like if the pets had the same name. 

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

- Answer: I'm just really satisified with the changes I made and how theres a noticeable difference from when I started.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

- Answer: If it were up to me, I wonder if a priority field functionality would be interesting enough to add. Since there are things like those when scheduling appointments in places that aren't just animal related. Like restaraunts or barbershops. 

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

- Answer: What I learned, or rather, what was reinforced is that AI is a very powerful tool that is only going to continue to get better, but you have to take what's written with a grain of salt. Which is why it's important to have projects such as these. 8/10! 
