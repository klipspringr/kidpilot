import smtplib
from google.cloud import vision
import io

# NOTE: This is not meant to be a working demo. Rather, this is the show the interaction
# between the application, XapiX, and 3rd party APIs.

#
# XAPIX INTERACTION WITH AIRBERLIN API
#

class AirBerlin:
  def __init__(api_key):
    self.api_key = api_key # We don't actually use api_key, just mocking
    
  def get_booking:
    return {
      'status': 'success',
      'data': {
        # fake customer data used, parameters removed for readability
        "booking_id": "12345",
        "random_id": "12345",
        "customer_addresses_0_email": "hello@google.com",
        "booking_date": "11/10/2016",
        "record_locator": "A1234",
        "passenger_type": "CHILD"
    }
  }

  def flight_segments(record_locator):
    return {
      "date": "12/10/16",
      "layover_time": 2.0 # added parameter for the sake of clarity. when used in real life,
      # this flight_segments field can be used to calculate layover time based on when flights
      # land and depart
    }

berlin_api = AirBerlin("api_key")

def get_layover_length():
  return berlin_api.flight_segments("A1234").layover_time

for passenger in berlin_api.get_booking.passenger_type: 
# look through all bookings for children. in real life, a better solution would be to run 
# this code after a booking has been made.
  if passenger == "CHILD":
    # introduce customer to KidPilot by sending parent an email introducing the application
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("service@airberlin.com", "password")
     
    msg = "We noticed that you're traveling with small children"
    server.sendmail("service@airberlin.com", AirBerlin.get_booking.customer_addresses_0_email , msg)
    server.quit()


if game_start == True:
  # ideally, this code would be run on the mobile application once the user has clicked the start game button.
  set_game_time_limit = get_layover_length % 10 # set the time limit to how many 10 minute chunks we can fit in the layover

#
# XAPIX INTERACTION WITH GOOGLE CLOUD IMAGE RECOGNITION API
#

client = vision.Client()

class GoogleCloudVision:
  def __init__(api_key):
    self.api_key = api_key # Again, we don't actually use api_key, just mocking

  def post_image(): # send over image to Google for recognition
    image = client.image('./image.jpg')
    landmarks = image.detect_landmarks()
    response = landmarks[0].description # landmarks[0].description contains a verbal description of the landmark 
                                        # found in the image. For example, a restaurant.

google_api = GoogleCloudVision("api_key")

if pictureTaken == True: # once a user has taken a picture, send it over to the Google Vision API for identification
  google_api.post_image
  return response
