import React, {useEffect} from 'react';
import {connect} from 'react-redux';
import AutoSizer from 'react-virtualized/dist/commonjs/AutoSizer';
import styled from 'styled-components';
import KeplerGl from 'kepler.gl';
import {addDataToMap, wrapTo} from 'kepler.gl/actions';
import {processGeojson} from 'kepler.gl/processors';
import config from './config';
import axios from 'axios'

const MAPBOX_TOKEN = "pk.eyJ1IjoiamRuaGl4IiwiYSI6ImNrd2s0NzF2ejFvb20yeW80NTlvenJ4OXMifQ.FxlxjZc-nN21l0s7N6EUwA"

var geojson = {
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
        "fillColor": [255, 0, 0] // use this to manually change the color
      }
    }
  ]
}

const StyledWrapper = styled.div`
  position: absolute;
  width: 100vw;
  height: 100vh;
`;

const wrapToMap = wrapTo('map1')
const apiURL = "http://18.189.79.44:8080/kepler/data"

function App({dispatch}) {

  useEffect(()=> {
    const interval = setInterval(() => {
      axios.get(apiURL).then(res => {
        console.log(res.data)

        var data = {
          datasets: {
            info: {
              label: 'input info',
              id: 'weather_data'
            },
            data: processGeojson(res.data)
          },
          options: {
            centerMap: false,
            readOnly: false
          },
          config: config
        }

        dispatch(wrapToMap(addDataToMap(data)))
      })
    }, 17500)
  }, [])

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
