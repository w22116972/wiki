# Efficient Documentation Management (Treating Docs Like Code)

> https://abseil.io/resources/swe-book/html/ch10.html

I. Integration into Engineering Workflow (The "Like Code" Principle)
Documentation changes must leverage and be incorporated into the existing developer workflow.
• Source Control: Documents deemed important must be placed under source control, ideally residing alongside the source code they document.
• Reviews and Changes: Documentation must undergo reviews for changes and should change with the code it documents.
• Issue Tracking: Issues or errors in documents must be tracked, similar to how bugs are tracked in code, often using existing bug tracking software.
• Changelists: Changes to documents are handled using the existing code review process and are made via changelists.
• Engineers as Maintainers: This integration enables engineers to file bugs, make changes, and send them for review, making documentation maintenance a similar experience to maintaining code.
II. Ownership and Accountability
Lack of clear ownership caused the failure of wiki-style approaches.
• Clear Ownership: Documents must have clear ownership responsible for maintaining them.
• Ownership Location: Placing documents within the source tree, alongside the code (e.g., in a g3doc directory), helps establish de facto ownership.
• Leveraging Ownership: Clear ownership makes it easier to manage documentation through existing developer workflows, such as bug tracking systems and code review tooling.
III. Canonical Status and Freshness
Documents must be accurate and up-to-date to be authoritative.
• Canonical Designation: It is crucial to designate canonical documentation—the primary source of truth—and consolidate or deprecate any conflicting or duplicate documents.
• Go/ Links: Using internal tools like "go/ links" can help a document establish itself as the canonical source on a given topic.
• Periodic Evaluation: Documentation should be periodically evaluated (measured for accuracy, freshness, etc.).
• Freshness Dates: Attach “freshness dates” to documentation (noting the last time it was reviewed). Metadata systems should send reminders if a document has not been touched, ensuring it is looked over from time to time.
IV. Standardization and Format
Standardization simplifies the writing and editing process for engineers.
• Common Format: The introduction of Markdown as a common documentation formatting language helped, as it made editing easier without requiring specialized expertise (like HTML or CSS).
• Structure and Rules: Like programming languages, documentation should have rules, a particular syntax, and style decisions to enforce consistency and improve clarity.
• Co-Location Frameworks: Using frameworks (such as g3doc) to embed documentation within code allows documents to exist side-by-side with the source code, making it easier to discover and maintain.
V. Document Scope and Purpose
Documents should adhere to a singular, defined purpose.
• Avoid Mixing Types: Do not mix different documentation types (e.g., conceptual information, API reference, and how-to guides) in one monolithic document.
• Focus on Purpose: A document should generally have a singular purpose and stick to it, breaking out pieces more logically if necessary.
• Landing Pages: Landing pages should function only as a traffic cop, containing only links to other information.
• Separate Audiences: Documents intended for internal providers (the team) should be kept separate from those intended for external customers (API users)