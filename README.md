1. Setup & Installation

Before running the application, ensure all dependencies are installed using:
pip install -r requirements.txt

2. Controls & Navigation

To ensure high-precision data collection, use the following interactive controls:

Left Click: Record the coordinates for the current mortality category. The target Month and Category are displayed in the window title.

Scroll Wheel: Zoom In/Out at the cursor position to inspect small or overlapping chart areas.

Right Click + Drag: Pan/Move the image while zoomed in.

'z' Key (Undo): Revert the last recorded point and return to the previous step.

's' Key (Skip): Skip the current data point if the data is missing or not visible. The system will automatically record 'N/A' in the dataset.

3. Data Output

All actions (clicks or skips) are saved in real-time to nightingale_progress.csv.

This persistence ensures that progress is never lost, even if the application is closed unexpectedly.

Short review:

Creating this app was pretty easy with the help of AI but understanding and fixing the bugs were the big challenges and took me a lot of time. Finally, when I understood the app and how it work (it worked smoothly), I was so proud of myself for making such an amazing app.
