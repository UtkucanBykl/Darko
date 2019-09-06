import React from "react";

const HEADERS = {
  Accept: "application/json",
  "Content-Type": "application/json",
  "Accept-Language": "tr"
};

const BASE_URL = "http://127.0.0.1:12345/";

class API {
  request(method, path, body, isFullPath = false) {
    return new Promise((resolve, reject) => {
      let url = `${BASE_URL}${path}`;
      const requestParams = {
        method,
        headers: HEADERS,
        body: undefined
      };
      if (body) {
        requestParams.body = JSON.stringify(body);
      }
      url = isFullPath ? path : url;
      fetch(url, requestParams)
        .then(response => {
          if (response.status < 300) {
            if (response._bodyInit === "") {
              return resolve(true);
            } else {
              return resolve(response.json());
            }
          } else {
            response
              .json()
              .then(errorResponse => {
                return reject(errorResponse);
              })
              .catch(error => {
                return reject(error);
              });
          }
        })
        .catch(err => {
          return reject(err);
        });
    });
  }
}

const api = new API();
export default api;
