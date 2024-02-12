"""This code adds vertices along the line at the specified interval and update the "Distance" field accordingly. Adjust the interval value as needed for your specific use case."""
import arcpy

# Set the workspace (adjust the path accordingly)
arcpy.env.workspace = r"C:\Users\Nolan\Documents\ArcGIS\PythonTestMap\MeterExtensionLines\MeterExtensionLines.gdb"

# Input polyline feature class
input_line_fc = "wMain"

# Add a field to store the distance along the line
#This line adds a new field named "Distance" to the input feature class to store the distance values.
arcpy.AddField_management(input_line_fc, "Distance", "DOUBLE")

def create_node():
    """Open an update cursor for the input line feature class
    This line opens an update cursor to iterate through each row of the input feature class. It retrieves the "SHAPE@" field (geometry) and the "Distance" field"""
    with arcpy.da.UpdateCursor(input_line_fc, ["SHAPE@", "Distance"]) as cursor:
        #This line starts a loop that iterates through each row in the feature class.
        for row in cursor:
            #These lines retrieve the geometry of the current row (line_geometry) and calculate its length (line_length).
            line_geometry = row[0]
            line_length = line_geometry.length

            """Define the interval (in feet) for adding nodes
            This line sets the interval at which you want to add vertices along the line. You can adjust this value based on your specific needs."""
            interval = 1.0  # Change this value according to your requirement

            """Add vertices along the line at the specified interval
            These lines start a loop to iterate through distances along the line at the specified interval."""
            new_vertices = []
            for distance in range(0, int(line_length) + 1, int(interval)):
                #These lines calculate a point along the line at the current distance and adds it to the list of new_vertices.
                point = line_geometry.positionAlongLine(distance).firstPoint
                new_vertices.append(point)

            # Update the geometry with the new vertices
            updated_line = arcpy.Polyline(arcpy.Array(new_vertices)) #This line creates a new Polyline object using the array of vertices.
            """These lines update the geometry of the current row with the new polyline containing added vertices, and update the "Distance"
            field with the last calculated distance. Finally, cursor.updateRow(row) is used to save the changes to the current row."""
            row[0] = updated_line
            row[1] = distance  # Update the "Distance" field
            cursor.updateRow(row)

def main():
    create_node()


if __name__ == "__main__":
    main()