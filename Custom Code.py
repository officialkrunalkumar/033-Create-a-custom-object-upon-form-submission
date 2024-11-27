import os, requests
def main(event):
  token = os.getenv("RevOps")
  custom_obj_id = "2-36882515"
  crate = event.get("inputFields").get("rate")
  cdate = event.get("inputFields").get("hs_createdate")
  custom_object_data = {
    "properties": {
      "nps": 10,
      "nps_survey_date": cdate
    }
  }
  api_url = f'https://api.hubapi.com/crm/v3/objects/{custom_obj_id}'
  headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
  }
  response = requests.post(api_url, json=custom_object_data, headers=headers)
  if response.status_code == 201:
    print("Custom object record created:", response.json())
  else:
    print("Error creating custom object record:", response.json())