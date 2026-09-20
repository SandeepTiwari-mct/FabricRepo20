# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "c11369b7-1b7b-41ea-a527-abbbe68bb642",
# META       "default_lakehouse_name": "LKH1",
# META       "default_lakehouse_workspace_id": "8c3ba8a3-3089-40e0-81c6-8ce9fe121304",
# META       "known_lakehouses": [
# META         {
# META           "id": "c11369b7-1b7b-41ea-a527-abbbe68bb642"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/sales.csv")
# df now is a Spark DataFrame containing CSV data from "Files/sales.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
