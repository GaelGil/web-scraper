const SneaksAPI = require('./sneaks-api/controllers/sneaks.controllers.js');
const sneaks = new SneaksAPI();
const fs = require('fs');


sneaks.getProductPrices("FY2903", function(err, product){
    if (err) {
        console.log(error);
      } 
    else {
        while (product) {
            
            for (const [key, value] of Object.entries(product.resellPrices)) {
                console.log(key);
                for (const [sec_key, sec_value] of Object.entries(product.resellPrices[key])) {
                    console.log(sec_key, sec_value);
                }
                console.log(' ');
              }

              product = false
        
            // console.log(product)
            // console.log(product.resellPrices)
            // console.log(product.shoeName)
            // console.log(product.brand)
            // console.log(product.silhoutte)
            // console.log(product.styleID)
            // console.log(product.make)
            // console.log(product.colorway)
            // console.log(product.retailPrice)
            // console.log(product.thumbnail)
            // console.log(product.releaseDate)


        }
    }

});