# Lateral-Line-HUD
Lateral Line creation for HUD mains

# Water Meter Main Connection Tool
Overview

This Python script connects water meters to a water main in ArcGIS Pro. It creates a new line feature class named "WaterMeterMainConnect2" in the specified geodatabase. The script calculates the closest point on the water main line for each water meter and creates a line connecting the water meter to the water main.

#### Prerequisites

ArcGIS Pro installed
Python installed with arcpy module
Usage
Open the script in Visual Studio Code.


#### Update the workspace path in the script:

python
Copy code
arcpy.env.workspace = r"C:\Users\Nolan\Documents\ArcGIS\PythonTestMap\MeterExtensionLines\MeterExtensionLines.gdb"
Update it with the path to your geodatabase.

####  Define the input point and line feature classes:

python
Copy code
point_fc = "wServiceConnection"
line_fc = "wMain"
output_fc = "WaterMeterMainConnect2"
Modify these variables if your feature classes have different names.

(Optional) Add fields to store attributes if needed:

python
Copy code
# arcpy.AddField_management(output_fc, "Field1", "TEXT")
Uncomment and modify this line if you need additional fields.

Run the script.

Script Explanation
The script uses arcpy module to interact with ArcGIS Pro.
It creates a new polyline feature class named "WaterMeterMainConnect2" in the specified geodatabase.
For each water meter point, it finds the closest point on the water main line and creates a line connecting the water meter to the water main.
Customization
You can add more fields to store attributes in the output feature class.
Modify the script according to your specific requirements.