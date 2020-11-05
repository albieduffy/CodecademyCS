export const fetchLocation = (lat, lng) => {
  return async (dispatch) => {
    try {
      const response = await fetch(
        `https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${lng}&result_type=country%7Clocality&key=${process.env.REACT_APP_google_key}`
      )
      const data = await response.json()
      if (data) { dispatch(setGeoLocation({location: data.results.formatted_address}))} //why??
    } catch (err) {
      throw new Error(err.message);
    }
  }
};
