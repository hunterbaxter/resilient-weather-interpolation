export default {
        visState: {
          layers: [
            {
              id: "weather_layer",
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
                },
                visualChannels: {
                  colorField: {
                    name: "field",
                    type: "int"
                  },
                  colorScale: "quantile",
                  sizeField: null,
                  sizeScale: "linear",
                  heightField: null,
                  heightScale: "linear",
                  radiusField: null,
                  radiusScale: "linear"
                }
              }
            }
          ]
        },
        mapState: {
          latitude: 36.1627,
          longitude: -86.78,
          zoom: 11,
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