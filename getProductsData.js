const SneaksAPI = require('./sneaks-api/controllers/sneaks.controllers.js');
const sneaks = new SneaksAPI();
const fs = require('fs');

//Product object includes styleID where you input it in the getProductPrices function
//getProductPrices(styleID, callback) takes in a style ID and returns sneaker info including a price map and more images of the product
sneaks.getProductPrices("FY2903", function(err, product){
    if (err) {
        console.log(error);
      } else {
    // console.log(product); 
    // for (let x =0; x < product.length; x++) {
    //     console.log(product[i])
    // }

    fs.writeFile("test.txt", product, function(err) {
        if (err) {
            console.log(err);
        }
    });
    }

})