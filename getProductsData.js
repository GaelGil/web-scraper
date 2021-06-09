const SneaksAPI = require('./sneaks-api/controllers/sneaks.controllers.js');
const sneaks = new SneaksAPI();
const fs = require('fs');


sneaks.getProductPrices("FY2903", function(err, product){
    if (err) {
        console.log(error);
      } 
    else {
        while (product) {
        console.log(product.shoeName)
        console.log(product.brand)
        console.log(product.silhoutte)
        console.log(product.styleID)
        console.log(product.make)
        console.log(product.colorway)
        console.log(product.retailPrice)
        console.log(product.thumbnail)
        console.log(product.releaseDate)
        var sizes = {} // dict to hold the sizes and price
        let counter = 0; // counter to hold how many sites we have data for
        // check if we have data
        if (product.resellPrices){
            // loop through all the sites
            for (const [key, value] of Object.entries(product.resellPrices)) {
                // check if the site is in the the json dict
                if (product.resellPrices[key]){
                    counter += 1 
                    // loop through each sites size and add pricing to sizes dictionary
                    for (const [sec_key, sec_value] of Object.entries(product.resellPrices[key])) {
                        if (!(sec_key in sizes)) {
                            sizes[sec_key] = sec_value;
                        }else {
                            sizes[sec_key] += sec_value;
                        }
                    }   
                }
                console.log(' ');
            }
        }
        // divide all prices by counter (how many sites we checked)
        for (const [key, value] of Object.entries(sizes)){
            sizes[key] = value/counter;
        }
        console.log(sizes);
        // end loop
        product = false
        }
    }

});