// Copyright (c) 2021 Uber Technologies, Inc.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.

import React, {useEffect} from 'react';
import {connect} from 'react-redux';
import AutoSizer from 'react-virtualized/dist/commonjs/AutoSizer';
import styled from 'styled-components';
import KeplerGl from 'kepler.gl';
import {addDataToMap, wrapTo} from 'kepler.gl/actions';
import {processGeojson} from 'kepler.gl/processors';

const MAPBOX_TOKEN = process.env.MapboxAccessToken; // eslint-disable-line


const sampledata = {
  "type":"FeatureCollection",
  "features":[
     {
        "type":"Feature",
        "geometry":{
           "type":"Polygon",
           "coordinates":[
              [
                 [
                  -86.66,
                    36.14
                 ],
                 [
                  -86.68,
                    36.145
                 ],
                 [
                   -86.67,
                    36.14
                 ],
                 [
                  -86.67,
                    36.138

                 ],
                 [
                  -86.66,
                    36.135
                 ],
                 [
                  -86.66,
                    36.14
                 ],
              ]
           ]
        },
        "properties": {
          "temp": "1",
          "prop1": {"this": "that"}
        }
     },
     {
        "type":"Feature",
        "geometry":{
           "type":"Polygon",
           "coordinates":[
              [
                [
                  -86.66-.02,
                    36.14
                ],
                [
                -86.68-.02,
                  36.145
                ],
                [
                  -86.67-.02,
                  36.14
                ],
                [
                -86.67-.02,
                  36.138

                ],
                [
                -86.66-.02,
                  36.135
                ],
                [
                  -86.66-.02,
                    36.14
                ],
              ]
           ]
        },
        "properties": {
          "temp": "10",
          "prop1": {"this": "that"}
        },
 
    },
    {
      "type":"Feature",
      "geometry":{
         "type":"Polygon",
         "coordinates":[
            [
              [
                -86.66-.01,
                  36.14-.02
                  ],
                [
                -86.68-.01,
                  36.145-.02
                ],
                [
                  -86.67-.01,
                  36.14-.02
                ],
                [
                -86.67-.01,
                  36.138-.02

                ],
                [
                -86.66-.01,
                  36.135-.02
                ],
                [
                  -86.66-.01,
                    36.14-.02
                ],
            ]
         ]
      },
      "properties": {
        "temp": "5",
        "prop1": {"this": "that"},
        // "fillColor": [255, 0, 0] # use this to manually change the color
      }
    }
  ]
}

const sampleconfig = {
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
            opacity: 0.55,
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
            // tempField: {
            //   name: "temp",
            //   type: "integer"
            // },
            // tempScale: "linear"
          }
        }
      }
    ]
  },
  mapState: {
    latitude: 36.1627,
    longitude: -86.78,
    zoom: 7,
  },
  mapStyle: {
    styleType: 'dark',
    // topLayerGroups: {},
    visibleLayerGroups: {
      label: true,
      road: true,
      border: false,
      // building: true,
      water: true,
      land: true
    }
  }
}

const sample = {
    datasets: {
      info: {
        label: 'input info',
        id: 'weather_data'
      },
      data: processGeojson(sampledata)
    },
    options: {
      centerMap: false,
      readOnly: false
    },
    config: sampleconfig
}




const StyledWrapper = styled.div`
  position: absolute;
  width: 100vw;
  height: 100vh;
`;

const wrapToMap = wrapTo('map1')
const App = ({dispatch}) => {

  useEffect(()=> {
    dispatch(wrapToMap(addDataToMap(sample)))
  }, [sampledata])

  return(
    <StyledWrapper>
      <AutoSizer>
        {({height, width}) => (
          <KeplerGl mapboxApiAccessToken={MAPBOX_TOKEN} id="map1" width={width} height={height} />
        )}
      </AutoSizer>
    </StyledWrapper>
  );

}

const mapStateToProps = state => state;
const dispatchToProps = dispatch => ({dispatch});

export default connect(mapStateToProps, dispatchToProps)(App);
