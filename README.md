Florence Nightingale's Rose Diagram — A Replication
The Story
Florence Nightingale's Rose Diagram is a landmark in the history of data visualization, created to persuade the British government to improve sanitary conditions in military hospitals. During the Crimean War, she observed that most soldiers died not from battle wounds, but from preventable infectious diseases. This diagram revolutionized the perception of public health, proving that visually presented data has the power to drive profound policy changes.

How the Data Was Collected
To replicate this diagram, I developed a Digitization App using Python and Matplotlib to extract data from the original image nightin.jpg. The application allows for high-precision navigation through scroll-to-zoom and pan features, enabling the selection of (x, y) pixel coordinates for each month and mortality category.

The Math and Visualization
Radii Calculation: I used the distances from the center (determined by click coordinates) to calculate the radius (r) for each section.

Area Proportionality: The area of each wedge was designed to be proportional to r 
2
 , ensuring the visual area accurately reflects the number of deaths.

Categorization: Each wedge is color-coded to distinguish between three causes: Preventable Zymotic diseases, Wounds, and Other causes.

User Manual & Interactive Controls
To ensure high-precision data collection, the application supports the following interactive controls:

Left Click: Record the coordinates for the current month and category (shown in the window title).

Scroll Wheel: Zoom In/Out at the cursor position for precise clicking.

Right Click + Drag: Pan/Move the image while zoomed in.

'z' Key (Undo): Revert the last recorded point and return to the previous step.

's' Key (Skip): Skip the current category if data is missing or not visible (records as 'N/A').

Auto-Save: All progress is saved in real-time to nightingale_progress.csv.

Key Insights
The Right Diagram (Before Reforms): Shows a massive area of deaths caused by infectious diseases (blue/black), far exceeding deaths from actual battle wounds.

The Left Diagram (After Reforms): The overall area shrank significantly once sanitary measures were implemented, proving the effectiveness of improving hospital environments.

Data and Policy: The diagram demonstrates that "preventable" diseases were the real enemy, leading to a complete restructuring of the British Army's medical system.

Personal Observation: Manually digitizing each data point made me appreciate the meticulousness of Nightingale’s data classification from over 150 years ago.

Technical Details
Language: Python 3

Libraries: Matplotlib, Pandas, Pillow, Numpy

Core Files:

your_application.py: The main digitizer tool with Zoom/Pan/Undo logic.

nightin.jpg: Original historical diagram for data extraction.

nightingale_progress.csv: The resulting dataset containing 72 digitized points.

walkthrough/output _image.png: Final visualization of the digitized progress.

How to Run
Clone this repository.

Install dependencies:

pip install -r requirements.txt

Run the application:

python your_application.py

What I Learned
Creating this app was a significant technical journey. While building the core features was straightforward with AI assistance, the real challenge lay in debugging the interactive event handlers for zoom and undo functions. I am incredibly proud of the final result—a smooth, functional tool that successfully bridged the gap between historical print and modern digital data.

References
Florence Nightingale, "Notes on Matters Affecting the Health, Efficiency, and Hospital Administration of the British Army", 1858.

Matplotlib Documentation for Event Handling.

Historical Data Visualization Archives.