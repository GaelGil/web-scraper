const SneaksAPI = require('./sneaks-api/controllers/sneaks.controllers.js');
const sneaks = new SneaksAPI();
const fs = require("fs");

let sneakers = [];
let data = ['name,colorway,release,retail,stockx,goat,stadium,flight,silhoutte,styleid,brand']

sneaks.getProducts("jordan 1 high 85", function(error, products){
  // show error if one occurs
  if (error){
      console.log(error)
  } else {
    // get every product
    for (let x =0; x < products.length; x++){
      product = products[x] // select a product
      let name = product.shoeName; 
      let found = sneakers.some(el => el.shoeName === name);
      // if its unique we add it to a list
      if (!found){
        sneakers.push(product);

        data.push(`${product.shoeName},${product.colorway},${product.releaseDate},${product.retailPrice},${product.lowestResellPrice.stockX},${product.lowestResellPrice.goat}, ${product.lowestResellPrice.stadiumGoods},${product.lowestResellPrice.flightClub},${product.silhoutte},${product.styleID},${product.brand}`)


        let csv = data.map((e) => {
            return e.replace(/;/g, ",");
        });


        fs.writeFile("./data.csv", csv.join("\r\n"), (err) => {
            console.log(err);
        })
      }
    }
  }
})


sneaks.getProducts("jordan 1", function(error, products){
  // show error if one occurs
  if (error){
      console.log(error)
  } else {
    // get every product
    for (let x =0; x < products.length; x++){
      product = products[x] // select a product
      let name = product.shoeName; 
      let found = sneakers.some(el => el.shoeName === name);
      // if its unique we add it to a list
      if (!found){
        sneakers.push(product);

        data.push(`${product.shoeName},${product.colorway},${product.releaseDate},${product.retailPrice},${product.lowestResellPrice.stockX},${product.lowestResellPrice.goat}, ${product.lowestResellPrice.stadiumGoods},${product.lowestResellPrice.flightClub},${product.silhoutte},${product.styleID},${product.brand}`)

        let csv = data.map((e) => {
            return e.replace(/;/g, ",");
        });
        
        fs.writeFile("./data.csv", csv.join("\r\n"), (err) => {
            console.log(err);
        })
      }
    }
  }
})


sneaks.getProducts("jordan", function(error, products){
  // show error if one occurs
  if (error){
      console.log(error)
  } else {
    // get every product
    for (let x =0; x < products.length; x++){
      product = products[x] // select a product
      let name = product.shoeName; 
      let found = sneakers.some(el => el.shoeName === name);
      // if its unique we add it to a list
      if (!found){
        sneakers.push(product);

        data.push(`${product.shoeName},${product.colorway},${product.releaseDate},${product.retailPrice},${product.lowestResellPrice.stockX},${product.lowestResellPrice.goat}, ${product.lowestResellPrice.stadiumGoods},${product.lowestResellPrice.flightClub},${product.silhoutte},${product.styleID},${product.brand}`)

        let csv = data.map((e) => {
            return e.replace(/;/g, ",");
        });
        
        fs.writeFile("./data.csv", csv.join("\r\n"), (err) => {
            console.log(err);
        })
      }
    }
  }
})



sneaks.getProducts("nike", function(error, products){
  // show error if one occurs
  if (error){
      console.log(error)
  } else {
    // get every product
    for (let x =0; x < products.length; x++){
      product = products[x] // select a product
      let name = product.shoeName; 
      let found = sneakers.some(el => el.shoeName === name);
      // if its unique we add it to a list
      if (!found){
        sneakers.push(product);

        data.push(`${product.shoeName},${product.colorway},${product.releaseDate},${product.retailPrice},${product.lowestResellPrice.stockX},${product.lowestResellPrice.goat}, ${product.lowestResellPrice.stadiumGoods},${product.lowestResellPrice.flightClub},${product.silhoutte},${product.styleID},${product.brand}`)

        let csv = data.map((e) => {
            return e.replace(/;/g, ",");
        });
        
        fs.writeFile("./data.csv", csv.join("\r\n"), (err) => {
            console.log(err);
        })
      }
    }
  }
})



sneaks.getProducts("nike dunk", function(error, products){
  // show error if one occurs
  if (error){
      console.log(error)
  } else {
    // get every product
    for (let x =0; x < products.length; x++){
      product = products[x] // select a product
      let name = product.shoeName; 
      let found = sneakers.some(el => el.shoeName === name);
      // if its unique we add it to a list
      if (!found){
        sneakers.push(product);

        data.push(`${product.shoeName},${product.colorway},${product.releaseDate},${product.retailPrice},${product.lowestResellPrice.stockX},${product.lowestResellPrice.goat}, ${product.lowestResellPrice.stadiumGoods},${product.lowestResellPrice.flightClub},${product.silhoutte},${product.styleID},${product.brand}`)


        let csv = data.map((e) => {
            return e.replace(/;/g, ",");
        });
        
        fs.writeFile("./data.csv", csv.join("\r\n"), (err) => {
            console.log(err);
        })
      }
    }
  }
})




sneaks.getProducts("off white", function(error, products){
  // show error if one occurs
  if (error){
      console.log(error)
  } else {
    // get every product
    for (let x =0; x < products.length; x++){
      product = products[x] // select a product
      let name = product.shoeName; 
      let found = sneakers.some(el => el.shoeName === name);
      // if its unique we add it to a list
      if (!found){
        sneakers.push(product);

        data.push(`${product.shoeName},${product.colorway},${product.releaseDate},${product.retailPrice},${product.lowestResellPrice.stockX},${product.lowestResellPrice.goat}, ${product.lowestResellPrice.stadiumGoods},${product.lowestResellPrice.flightClub},${product.silhoutte},${product.styleID},${product.brand}`)

        let csv = data.map((e) => {
            return e.replace(/;/g, ",");
        });
        
        fs.writeFile("./data.csv", csv.join("\r\n"), (err) => {
            console.log(err);
        })
      }
    }
  }
})



sneaks.getProducts("adidas", function(error, products){
  // show error if one occurs
  if (error){
      console.log(error)
  } else {
    // get every product
    for (let x =0; x < products.length; x++){
      product = products[x] // select a product
      let name = product.shoeName; 
      let found = sneakers.some(el => el.shoeName === name);
      // if its unique we add it to a list
      if (!found){
        sneakers.push(product);

        data.push(`${product.shoeName},${product.colorway},${product.releaseDate},${product.retailPrice},${product.lowestResellPrice.stockX},${product.lowestResellPrice.goat}, ${product.lowestResellPrice.stadiumGoods},${product.lowestResellPrice.flightClub},${product.silhoutte},${product.styleID},${product.brand}`)



        let csv = data.map((e) => {
            return e.replace(/;/g, ",");
        });
        
        fs.writeFile("./data.csv", csv.join("\r\n"), (err) => {
            console.log(err);
        })
      }
    }
  }
})




sneaks.getProducts("yeezy", function(error, products){
  // show error if one occurs
  if (error){
      console.log(error)
  } else {
    // get every product
    for (let x =0; x < products.length; x++){
      product = products[x] // select a product
      let name = product.shoeName; 
      let found = sneakers.some(el => el.shoeName === name);
      // if its unique we add it to a list
      if (!found){
        sneakers.push(product);

        data.push(`${product.shoeName},${product.colorway},${product.releaseDate},${product.retailPrice},${product.lowestResellPrice.stockX},${product.lowestResellPrice.goat}, ${product.lowestResellPrice.stadiumGoods},${product.lowestResellPrice.flightClub},${product.silhoutte},${product.styleID},${product.brand}`)

        let csv = data.map((e) => {
            return e.replace(/;/g, ",");
        });
        
        fs.writeFile("./data.csv", csv.join("\r\n"), (err) => {
            console.log(err);
        })
      }
    }
  }
})


