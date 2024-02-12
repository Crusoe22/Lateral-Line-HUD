
'''Create python code that connects a water meter to a water main in ArcGIS pro'''

import arcpy

# Set the workspace
arcpy.env.workspace = r"C:\Users\Nolan\Documents\ArcGIS\PythonTestMap\MeterExtensionLines\MeterExtensionLines.gdb"  # Update with the path to your geodatabase

# Define the input point and line feature classes
point_fc = "wServiceConnection"
line_fc = "wMain"
output_fc = "WaterMeterMainConnect2"

# Create a new line feature class
#Creates a new polyline feature class named WaterMeterMainConnect in the specified geodatabase.
arcpy.CreateFeatureclass_management(arcpy.env.workspace, output_fc, "POLYLINE")


# Add fields to store attributes if needed
# arcpy.AddField_management(output_fc, "Field1", "TEXT")


def draw_line():
    
    '''Create an insert cursor for the new WaterMeterMainConnect feature class. Creates an insert cursor to add rows (features) to the WaterMeterMainConnect 
    feature class. It specifies that the cursor will be working with the SHAPE@ (geometry) and "Shape_Length" (length of the line) fields.'''
    with arcpy.da.InsertCursor(output_fc, ["SHAPE@", "Shape_Length"]) as insert_cursor:  # Add more fields if needed, #"Field1" 
        
        # Iterate through Meter points
        #Creates a search cursor to iterate through the features (rows) in the 
        #WaterMeterPythonTest feature class. It extracts the SHAPE@XY (centroid coordinates) and SHAPE@ (geometry) fields.
        with arcpy.da.SearchCursor(point_fc, ["SHAPE@XY", "SHAPE@"]) as cursor:
            
            # Iterates through each row in the WaterMeterPythonTest feature class 
            # and extracts the centroid coordinates and geometry of the water meter point.
            for row in cursor:
                meter_point_xy = row[0]
                meter_point_geometry = row[1]

                # Create a search cursor to iterate through WaterLine vertices
                #Creates a search cursor to iterate through the features in the WaterMainPythonTest feature class, extracting the geometry field.
                with arcpy.da.SearchCursor(line_fc, ["SHAPE@"]) as line_cursor: 
                    min_distance = float("inf")
                    closest_point = None

                    # Iterate through line vertices
                    # Iterates through the vertices of the water main line features to find the closest point to each water meter point.
                    for line_row in line_cursor:
                        line_geometry = line_row[0]
                        for part in line_geometry:
                            for pnt in part:
                                distance = meter_point_geometry.distanceTo(pnt) # Calculates the distance between the water meter point and the current vertex on the water main line.

                                # Update closest point if a closer one is found
                                # Updates the closest_point if the current vertex is closer to the water meter point than the previously closest vertex.
                                if distance < min_distance:
                                    min_distance = distance
                                    closest_point = pnt

                    # Create a new line and insert it into WaterMeterMainConnect
                    line_array = arcpy.Array([meter_point_geometry.centroid, closest_point]) # Creates a new line geometry using an array of two points:
                    line = arcpy.Polyline(line_array) #the centroid of the water meter point and the closest point on the water main line
                    insert_cursor.insertRow([line, "Value1"])  # Inserts a new row into the WaterMeterMainConnect feature class with the created line geometry and attribute value (Value1)
                    # Add attribute values as needed
                    # You can add more fields and update the insertRow accordingly

    print("Lines created successfully in WaterMeterMainConnect.")

def main():
    draw_line()

if __name__ == "__main__":
    main()