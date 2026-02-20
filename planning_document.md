The raw ideas were 100% mine, I used AI to inhence the english and made the plan in formal language.

Implementation Script: AI Prompting Strategy

Below is the summary of the prompts used to guide the AI in developing this Digitizer application, categorized by functional goals:

Core Prompt: Create an app by code to load the image and show the coordinate of the image and print out the coordinate when clicked by x,y coordinate system by pixel of the image nightin.jpg


1. Image Navigation & Precision (Zoom & Pan)

Goal: To ensure high accuracy when selecting data points, especially for smaller wedges in the diagram.

Prompt: "Modify the code to use the matplotlib library. Implement a scroll-to-zoom feature at the current cursor position and right-click-and-drag (pan) to move the image. This allows for precise coordinate selection for all 24 months."

2. Systematic Data Workflow (72-Point Collection)

Goal: To maintain a strict chronological order and prevent confusion between the 24 months and 3 mortality categories.

Prompt: "Create a structured sequence for 24 months (April 1854 to March 1856). For each month, the app must guide me to click in a specific order: 1. Other causes, 2. Wounds, 3. Zymotic diseases. Update the window title dynamically to show the current month and the required category color."

3. Real-Time Data Persistence (Auto-Save)

Goal: To prevent data loss and allow for immediate verification of the captured coordinates.

Prompt: "Implement real-time logging. Every click should immediately print the data row to the terminal and auto-save/update the nightingale_progress.csv file. I want to see the CSV file filling up as I work, ensuring no data is lost if the application closes."

4. Error Handling & Flexibility (Undo & Skip)

Goal: To allow corrections for accidental clicks and handle months with missing or zero data.

Prompt: * Undo: "Bind the 'z' key to undo the last point, removing the marker from the image and deleting the corresponding entry from the DataFrame/CSV."

Skip: "Disable default Matplotlib shortcuts to free up the 's' key. Use 's' to skip a category, filling the data cell with 'N/A' and advancing to the next target. This is essential for months where certain data is not visible on the original chart."

5. Visual Feedback System

Goal: To provide clear visual confirmation of which areas have already been digitized.

Prompt: "Every time a point is captured, draw a persistent color-coded marker (Blue, Red, or Black) on the image with a sequence number label. This helps me track my progress and avoid duplicate clicks."