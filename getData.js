const SneaksAPI = require('sneaks-api');
const sneaks = new SneaksAPI();
const fs = require('fs'); // to write to csv
// const time = require('') // to get todays date



sneaks.getProductPrices("FY2903", function(err, product){
    if (err) {
        console.log(error);
      } 
    else {
        while (product) {
        // important data to get
        // console.log(product.shoeName)
        // console.log(product.brand)
        // console.log(product.styleID)
        // console.log(product.colorway)
        // console.log(product.retailPrice)
        // console.log(product.thumbnail)
        // console.log(product.releaseDate)

        var sizes = {} // dict to hold the sizes and price

        // check if we have any data
        if (product.resellPrices){
            var siteCounter = 0; // counter to hold how many sites we have data for
            // loop through `product.resellPrices` (a list of dictionaries)
            for (const [site, prices] of Object.entries(product.resellPrices)) {
                if (product.resellPrices[site]){
                    siteCounter += 1
                    // loop through every available site in to check its prices
                    for (const[size, price] of Object.entries(product.resellPrices[site])){
                        // if we have not yet seen it add it to our dictionary
                        if (!(size in sizes) && price != NaN){
                            console.log(`size: ${size} price: ${price}`)
                            sizes[size] = price;
                        } else if (size in sizes && price != NaN){
                            sizes[size] += price;
                        }
                    }
                }
            }
        }

        console.log(sizes);
        product = false
        }
        
    }

});