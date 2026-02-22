# Florence Nightingale's Rose Diagram — A Replication

![Logo](assets/logo.png)

## The Story

The Crimean War presented a devastating sanitary reform crisis where more soldiers were dying from preventable infections than from battle wounds. To communicate this urgency to officials, Florence Nightingale developed the "Rose Diagram," a groundbreaking polar area chart that made the invisible causes of mortality impossible to ignore. This visualization ultimately revolutionized British military policy and laid the foundation for modern evidence-based healthcare practices.

## How the Data Was Collected

I built a Python app that let me click 4 key points on each month in Nightingale's original diagram image. The app saved these pixel coordinates as a JSON file to ensure accuracy. I then used Python to convert those coordinates into radii and proportional areas for different causes of death, making the historical data ready for modern visualization.

## The Math and Visualization

-   **Distance to Radii**: I used the distances from the center of the diagram to compute the radii for each wedge.
-   **Area Proportionality**: The areas of the wedges are proportional to $r^2$, ensuring the visual impact matches the actual data.
-   **Encoding Causes**: Each wedge encodes deaths from three different causes: preventable diseases, wounds, and other causes.

## The Visualization

![Rose Diagram](walkthrough/nightingale_rose.png)

## Key Insights

-   The left diagram (before reforms) reveals that preventable "zymotic" diseases were the leading cause of death, far exceeding deaths from actual combat.
-   The right diagram (after reforms) shows a dramatic reduction in the size of the wedges, illustrating how much mortality fell after sanitary improvements.
-   This visualization demonstrates that data-driven policy change happens when complex statistics are transformed into a clear, persuasive visual narrative.
-   **Extra Observation**: It is striking how the blue areas (infectious diseases) almost disappear in the final months compared to the start of the war.

## Technical Details

-   **Language**: Python
-   **Libraries**: `matplotlib`, `pandas`, `numpy`, `json`
-   **Files**:
    -   `src/digitize_app.py`
    -   `src/plot_rose.py`
    -   `data/coordinates.json`
    -   `data/nightingale_computed.csv`

## How to Run

1.  **Clone** this repository to your local machine.
2.  **Create and activate** a virtual environment.
3.  **Install requirements** (if you have a `requirements.txt`).
4.  **Run the plotting script**: `python src/plot_rose.py`

## What I Learned

Through this project, I learned the technical challenge of extracting structured data from a 150-year-old image using Python and coordinate math. I also realized that data visualization is a bridge between raw numbers and social change, showing how a single chart can influence government policy to save lives.

## References

-   Nightingale, F. (1858). *Notes on Matters Affecting the Health, Efficiency, and Hospital Administration of the British Army*.
-   [Add your extra source links here]
