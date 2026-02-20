# Florence Nightingale's Rose Diagram — A Replication

![Rose Diagram](walkthrough/output%20_image.png)

## The Story
Florence Nightingale's Rose Diagram is a landmark in the history of data visualization, created to persuade the British government to improve sanitary conditions in military hospitals. During the Crimean War, she observed that most soldiers died not from battle wounds, but from preventable infectious diseases. This diagram revolutionized the perception of public health, proving that visually presented data has the power to drive profound policy changes.

## How the Data Was Collected
To replicate this diagram, I developed a Digitization App using Python and Matplotlib to extract data from the original image nightin.jpg. 

* Precision: The application allows for high-precision navigation through scroll-to-zoom and pan features.
* Methodology: Enabled the selection of (x, y) pixel coordinates for each of the 72 data points (24 months x 3 categories).
* Persistence: Data was captured in real-time and saved to CSV to ensure zero data loss.

## The Math and Visualization
* Radii Calculation: Distances from the center to the clicked coordinates determine the radius (r).
* Area Proportionality: The area of each wedge is proportional to r squared, ensuring visual accuracy relative to mortality numbers.
* Categorization:
    * Blue: Preventable Zymotic diseases
    * Red: Wounds
    * Black: Other causes

## User Manual and Interactive Controls
The application includes a specialized control system for efficient digitizing:

| Action | Control | Description |
| :--- | :--- | :--- |
| Record | Left Click | Capture coordinates for the current month and category. |
| Zoom | Scroll Wheel | Zoom in/out at the current cursor position for precision. |
| Pan | Right Click + Drag | Move the image while zoomed in to navigate the chart. |
| Undo | 'z' Key | Delete the last recorded point and return to the previous step. |
| Skip | 's' Key | Skip a category (records as 'N/A') if data is missing or not visible. |

## Key Insights
* Before Reforms: The massive area of preventable deaths (blue) significantly outweighs deaths from actual battlefield wounds.
* After Reforms: The dramatic reduction in the diagram's area proves the life-saving impact of sanitary improvements.
* Personal Observation: Manually digitizing these points highlighted the meticulous care Nightingale took in her original 1858 research and the complexity of her data classification.

## Technical Details
* Language: Python 3
* Libraries: matplotlib, pandas, Pillow, numpy
* Core Files:
    * your_application.py: The digitizer tool with custom event handling.
    * nightingale_progress.csv: Resulting dataset containing 72 digitized points.
    * nightin.jpg: Original historical source image.

## How to Run
1. Clone the repository.
2. Install dependencies:  
   pip install -r requirements.txt
3. Run the application:  
   python your_application.py

## What I Learned
Creating this app was a significant technical journey. While building the core features was straightforward, the real challenge lay in debugging the interactive event handlers for the zoom, pan, and undo functions. I am proud of the final result—a functional tool that successfully bridges the gap between historical print and modern digital data.