(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
var $, createMap;

$ = window.$;

createMap = require("./map.coffee");

$.fn.createMap = function() {
  this.show();
  createMap(this);
  return this;
};

$(".map").each(function() {
  return $(this).createMap();
});

$("body").on("submit", "form", function(e) {
  var url;
  e.preventDefault();
  url = $(this).attr("action");
  return $.ajax({
    url: url,
    type: "POST",
    data: $(this).serialize(),
    success: (data) => {
      return $(this).replaceWith(data);
    }
  });
});


},{"./map.coffee":2}],2:[function(require,module,exports){
var google, style;

google = window.google;

style = [
  {
    stylers: [
      {
        hue: "#00aaff"
      },
      {
        saturation: -10
      },
      {
        gamma: 1.2
      },
      {
        lightness: 5
      }
    ]
  },
  {
    featureType: "landscape.natural",
    stylers: [
      {
        visibility: "on"
      },
      {
        color: "#a2d398"
      }
    ]
  },
  {
    featureType: "landscape.man_made",
    stylers: [
      {
        visibility: "on"
      },
      {
        color: "#BFDD9D"
      }
    ]
  },
  {
    featureType: "transit",
    elementType: "labels",
    stylers: [
      {
        visibility: "off"
      }
    ]
  },
  {
    featureType: "poi",
    elementType: "labels",
    stylers: [
      {
        visibility: "off"
      }
    ]
  },
  {
    featureType: "water",
    stylers: [
      {
        visibility: "on"
      },
      {
        color: "#d3eef5"
      }
    ]
  },
  {
    featureType: "water",
    elementType: "labels",
    stylers: [
      {
        visibility: "off"
      }
    ]
  },
  {
    featureType: "road",
    elementType: "labels.icon",
    stylers: [
      {
        visibility: "off"
      }
    ]
  },
  {
    featureType: "road",
    elementType: "labels.text.fill",
    stylers: [
      {
        visibility: "on"
      },
      {
        lightness: 24
      }
    ]
  },
  {
    featureType: "road",
    elementType: "geometry.fill",
    stylers: [
      {
        color: "#78cfed"
      }
    ]
  },
  {
    featureType: "road.highway",
    elementType: "geometry.fill",
    stylers: [
      {
        color: "#9b8ac1"
      }
    ]
  },
  {
    featureType: "road.highway",
    elementType: "geometry.stroke",
    stylers: [
      {
        color: "#799ECC"
      }
    ]
  },
  {
    featureType: "road.highway.controlled_access",
    elementType: "geometry.stroke",
    stylers: [
      {
        color: "#8067ad"
      }
    ]
  },
  {
    featureType: "road.highway.controlled_access",
    elementType: "geometry.fill",
    stylers: [
      {
        color: "#9a8cbd"
      }
    ]
  }
];

module.exports = function(el) {
  var circle, data, loc, map, mapOptions, marker;
  data = window.JSON.parse(el.text());
  el.text("");
  loc = new google.maps.LatLng(data[0], data[1]);
  mapOptions = {
    zoom: 12,
    center: loc,
    styles: style,
    scrollwheel: false,
    navigationControl: false,
    mapTypeControl: false,
    zoomControl: true,
    zoomControlOptions: {
      style: google.maps.ZoomControlStyle.SMALL,
      position: google.maps.ControlPosition.RIGHT_TOP
    },
    streetViewControl: false
  };
  map = new google.maps.Map(el[0], mapOptions);
  circle = {
    path: google.maps.SymbolPath.CIRCLE,
    fillColor: "#7d6aaa",
    fillOpacity: 0.8,
    scale: 6,
    strokeColor: "#5d3393",
    strokeWeight: 2
  };
  return marker = new google.maps.Marker({
    position: loc,
    icon: circle,
    map: map
  });
};


},{}]},{},[1]);
