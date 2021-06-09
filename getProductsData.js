const SneaksAPI = require('./sneaks-api/controllers/sneaks.controllers.js');
const sneaks = new SneaksAPI();
const fs = require('fs');

function getPrices(product) {
    while (product) {
        // console.log(product.shoeName)
        // console.log(product.brand)
        // console.log(product.silhoutte)
        // console.log(product.styleID)
        // console.log(product.make)
        // console.log(product.colorway)
        // console.log(product.retailPrice)
        // console.log(product.thumbnail)
        // console.log(product.releaseDate)
        var sizes = {}
        if (product.resellPrices){
            for (const [key, value] of Object.entries(product.resellPrices)) {
                for (const [sec_key, sec_value] of Object.entries(product.resellPrices[key])) {
                    if (!(sec_key in sizes)) {
                        sizes[sec_key] = sec_value;
                        }else {
                            size[sec_key] += sec_value
                        }
                            // console.log(sec_key, sec_value);

                }   
                console.log(' ');
            }
        }
        product = false
    }
    console.log(sizes)
}


function get_product_details() {
    sneaks.getProductPrices("FY2903", function(err, product){
        if (err) {
            // console.log(error);
          } 
        else {
            getPrices(product);
        }
    });
}

get_product_details();

// function searchQueries(data) {
//     for (let i = 0; i < data.length; i++) {
//         sneaks.getProducts(data[i], function(error, products) {
//             // show error if it occurs
//             if (error) {
//             //   console.log(error);
//             } else {
//               // get every product
//               for (let x =0; x < products.length; x++) {
//                 product = products[x]; // select a product
//                 const stlye_id = product.styleID;
//                 while(product) {
//                     get_product_details(stlye_id)
//                     product = false;
//                 } 
//               }
//             }
//         });
//     }
// }

// const list_of_queries = ['jordan 1', 'jordan', 'nike', 'adidas', 'yeezy', 'off white', 'jordan 1 high 85']
// searchQueries(list_of_queries);