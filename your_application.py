import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import numpy as np
import os

# Disable default key bindings
if 's' in plt.rcParams['keymap.save']:
    plt.rcParams['keymap.save'].remove('s')

class NightingaleDigitizer:
    def __init__(self, image_path, output_file='output_data.csv'):
        self.image_path = image_path
        self.output_file = output_file
        
        # Initialize Data Structure
        months = pd.date_range(start='1854-04-01', end='1856-03-01', freq='MS')
        self.months = [m.strftime('%B %Y') for m in months]
        self.categories = ['Preventable or Mitigable Zymotic diseases', 'Wounds', 'Other causes']
        
        # Total points to collect: 24 months * 3 categories = 72 points
        self.total_points = len(self.months) * len(self.categories)
        self.current_idx = 0
        
        # DataFrame to store results
        self.df = pd.DataFrame(index=self.months, columns=self.categories)
        
        # Data storage for plotting (x, y coordinates)
        self.coords = [] # List of tuples: (month, category, x, y, marker_object)

        # Matplotlib setup
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        try:
            self.img = mpimg.imread(self.image_path)
            self.ax.imshow(self.img)
        except Exception as e:
            print(f"Error loading image: {e}")
            return

        self.ax.set_title("Nightingale Digitizer")
        self.ax.axis('off')

        # Event connections
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('key_press_event', self.on_key)
        self.fig.canvas.mpl_connect('scroll_event', self.zoom_factory)
        self.fig.canvas.mpl_connect('button_press_event', self.pan_on_press)
        self.fig.canvas.mpl_connect('button_release_event', self.pan_on_release)
        self.fig.canvas.mpl_connect('motion_notify_event', self.pan_on_motion)
        
        # Pan/Zoom state
        self.press = None
        
        # Initial GUI Update
        self.update_guidance()
        
        print("Starts Nightingale Digitizer.")
        print("Controls:")
        print("  Left Click: Record point")
        print("  Right Click + Drag: Pan")
        print("  Scroll: Zoom")
        print("  'z': Undo last point")
        print("  's': Skip current point")
        
        plt.show()

    def get_current_target(self):
        if self.current_idx >= self.total_points:
            return None, None
        
        month_idx = self.current_idx // len(self.categories)
        cat_idx = self.current_idx % len(self.categories)
        
        return self.months[month_idx], self.categories[cat_idx]

    def update_guidance(self):
        month, category = self.get_current_target()
        if month:
            title = f"Click for: {month} - {category} ({self.current_idx + 1}/{self.total_points})"
            self.ax.set_title(title, color='blue', fontweight='bold')
            print(f"NEXT: {month} - {category}")
        else:
            self.ax.set_title("All points collected! File saved.", color='green', fontweight='bold')
            print("Done! All points collected.")
        self.fig.canvas.draw()

    def on_click(self, event):
        # Ignore clicks outside axes or if using right click (pan)
        if event.inaxes != self.ax or event.button != 1:
            return
            
        # Ignore if finished
        if self.current_idx >= self.total_points:
            return

        month, category = self.get_current_target()
        
        # 1. Record Data
        x, y = event.xdata, event.ydata
        
        # Plot marker
        color_map = {
            'Preventable or Mitigable Zymotic diseases': 'blue', 
            'Wounds': 'red', 
            'Other causes': 'black'
        }
        marker, = self.ax.plot(x, y, 'o', color=color_map[category], markersize=5, markeredgecolor='white')
        
        # Store data
        self.coords.append({
            'month': month,
            'category': category,
            'x': x,
            'y': y,
            'marker': marker
        })
        
        # Update DataFrame
        # Store as string tuple or just x/y? The prompt asks for "data row". 
        # Usually for digitization we want the value, but here we just have coordinates.
        # I will store the coordinate tuple for now.
        self.df.at[month, category] = (x, y)
        
        # 2. Immediate Terminal Update
        print(f"Recorded: {month} | {category} | x={x:.2f}, y={y:.2f}")
        
        # 3. Auto-Save
        self.save_progress()

        # Advance index
        self.current_idx += 1
        
        # 4. Update Guidance
        self.update_guidance()

    def on_key(self, event):
        if event.key == 'z':
            self.undo()
        elif event.key == 's':
            self.skip_point()

    def skip_point(self):
        # Ignore if finished
        if self.current_idx >= self.total_points:
            return

        month, category = self.get_current_target()
        
        # Store data with None marker and "N/A" coordinates
        self.coords.append({
            'month': month,
            'category': category,
            'x': 'N/A',
            'y': 'N/A',
            'marker': None
        })
        
        # Update DataFrame
        self.df.at[month, category] = 'N/A'
        
        # Immediate Terminal Update
        print(f"Skipped: {month} | {category}")
        
        # Auto-Save
        self.save_progress()

        # Advance index
        self.current_idx += 1
        
        # Update Guidance
        self.update_guidance()

    def undo(self):
        if self.current_idx == 0:
            print("Nothing to undo.")
            return

        # Get last entry
        last_entry = self.coords.pop()
        
        # Remove from plot if marker exists
        if last_entry['marker']:
            last_entry['marker'].remove()
        
        # Remove from DataFrame
        self.df.at[last_entry['month'], last_entry['category']] = np.nan
        
        # Decrement index
        self.current_idx -= 1
        
        # Save updated state
        self.save_progress()
        
        status = "Skipped" if last_entry['marker'] is None else "Recorded"
        print(f"Undid ({status}): {last_entry['month']} - {last_entry['category']}")
        self.update_guidance()

    def save_progress(self):
        try:
            self.df.to_csv(self.output_file)
        except Exception as e:
            print(f"Error saving progress: {e}")

    # Zoom functionality
    def zoom_factory(self, event):
        if event.inaxes != self.ax: return
        base_scale = 1.2
        
        # get the current x and y limits
        cur_xlim = self.ax.get_xlim()
        cur_ylim = self.ax.get_ylim()
        
        xdata = event.xdata # get event x location
        ydata = event.ydata # get event y location
        
        if event.button == 'up':
            # deal with zoom in
            scale_factor = 1/base_scale
        elif event.button == 'down':
            # deal with zoom out
            scale_factor = base_scale
        else:
            # deal with something that should never happen
            scale_factor = 1
            print(event.button)
            
        # set new limits
        new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
        new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor
        
        relx = (cur_xlim[1] - xdata)/(cur_xlim[1] - cur_xlim[0])
        rely = (cur_ylim[1] - ydata)/(cur_ylim[1] - cur_ylim[0])
        
        self.ax.set_xlim([xdata - new_width * (1-relx), xdata + new_width * relx])
        self.ax.set_ylim([ydata - new_height * (1-rely), ydata + new_height * rely])
        self.fig.canvas.draw()

    # Pan functionality
    def pan_on_press(self, event):
        if event.button == 3: # Right click
            self.press = event.xdata, event.ydata

    def pan_on_release(self, event):
        self.press = None
        self.fig.canvas.draw()

    def pan_on_motion(self, event):
        if self.press is None or event.inaxes != self.ax: return
        dx = event.xdata - self.press[0]
        dy = event.ydata - self.press[1]
        
        cur_xlim = self.ax.get_xlim()
        cur_ylim = self.ax.get_ylim()
        
        self.ax.set_xlim(cur_xlim[0] - dx, cur_xlim[1] - dx)
        self.ax.set_ylim(cur_ylim[0] - dy, cur_ylim[1] - dy)
        self.fig.canvas.draw()

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(current_dir, "nightin.jpg")
    
    if not os.path.exists(img_path):
        print(f"Error: {img_path} not found.")
    else:
        app = NightingaleDigitizer(img_path)
