import functions_framework

@functions_framework.cloud_event
def print_logs(cloud_event):
  file_data = cloud_event.data
  object_name = file_data["name"]
  bucket_name = file_data["bucket"]

  print("got object ")
  print(object_name)
  print("got bucket ")
  print(bucket_name)