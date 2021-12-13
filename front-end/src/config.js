export default {
        visState: {
          layers: [
            {
              id: "321",
              type: "geojson",
              config: {
                dataId: 'weather_data',
                label: "Weather",
                columns: {
                  geojson: "_geojson"
                },
                isVisible: true,
                visConfig: {
                  opacity: 0.05,
                  thickness: 2,
                  colorRange: {
                    name: "Test Range",
                    type: "sequential",
                    category: "Uber",
                    colors: [
                      "#DBE9F5",
                      "#AFC6D9",
                      "#83A3BE",
                      "#5880A2",
                      "#2C5D87",
                      "#003A6B"
                    ],
                    reversed: false
                  },
                  radius: 10,
                  stroked: false,
                  filled: true,
                  tempRange: [
                    0, 10
                  ]
                },
                visualChannels: {
                  colorField: {
                    name: "temp",
                    type: "int"
                  },
                  colorScale: "quantile",
                }
              }
            }
          ]
        },
        mapState: {
          latitude: 36.1627,
          longitude: -86.78,
          zoom: 10,
        },
        mapStyle: {
          styleType: 'dark',
          visibleLayerGroups: {
            label: true,
            road: true,
            border: false,
            water: true,
            land: true
          }
        }
      }