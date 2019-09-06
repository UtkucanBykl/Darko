import React, { useState, useEffect } from "react";
import API from "../helpers/api";

export default function Index() {
  const [data, setData] = useState([]);

  useEffect(() => {
    API.request("GET", "nodes/").then(response => {
      setData(response.data);
    });
  }, []);

  return (
    <div>
      {data.map(item => (
        <h1>{item.name}</h1>
      ))}
    </div>
  );
}
