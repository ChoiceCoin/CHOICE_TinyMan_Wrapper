import fetch from 'node-fetch';
import { Client, Intents } from 'discord.js';
import express from 'express';

const app = express();

const port = process.env.PORT || 3500;

import dotenv from 'dotenv'
 dotenv.config();

const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

const serverID = '859233439168069682';
const priceUpdateChannelID = '945403182413127690';
const liquidityChannelID = '907444405831598110';
const algoStakeChannelID = '937528942221463573';
const distributionChannelID = '915421294563061770'
const rewardChannelID = '915403991322624050';



let choice_price;
let choice_market_cap;
let algo_price;
let yieldly_price;
let algostake_price;
let defly_price;
let tiny_price;


app.get('/', (req,res) => {
    res.json('Choice Coin V2 Bot 🤖 is up and running')
})

// getting choice price from liveCoinWatch API
const getChoicePrice =  async () => {
 await fetch("https://api.livecoinwatch.com/coins/single", {
        method: "POST",
        headers: {
          "content-type": "application/json",
          "x-api-key": process.env.API_KEY,
        },
        body: JSON.stringify({
          currency: "USD",
          code: "CHOICE",
          meta: true,
        }),
      }).then(resp => resp.json())
      .then(data => {
        choice_price = data.rate.toFixed(6)
        choice_market_cap = data.cap
        
      })
      
}


//getting algo price from LiveCoinWatch API
const getAlgoPrice = async () => {
    await fetch("https://api.livecoinwatch.com/coins/single", {
        method: "POST",
        headers: {
          "content-type": "application/json",
          "x-api-key": process.env.API_KEY,
        },
        body: JSON.stringify({
          currency: "USD",
          code: "ALGO",
          meta: true,
        }),
      }).then(resp => resp.json())
      .then(data => {
        algo_price = data.rate.toFixed(4)
        
      })
}



// get yieldy price

const getYieldlyPrice = async () => {
    await fetch("https://api.livecoinwatch.com/coins/single", {
        method: "POST",
        headers: {
          "content-type": "application/json",
          "x-api-key": process.env.API_KEY,
        },
        body: JSON.stringify({
          currency: "USD",
          code: "YLDY",
          meta: true,
        }),
      }).then(resp => resp.json())
      .then(data => {
        yieldly_price = data.rate.toFixed(6)
        
      })
}



// get algostake price

const getSTKEPrice = async () => {
    await fetch("https://api.livecoinwatch.com/coins/single", {
        method: "POST",
        headers: {
          "content-type": "application/json",
          "x-api-key": process.env.API_KEY,
        },
        body: JSON.stringify({
          currency: "USD",
          code: "STKE",
          meta: true,
        }),
      }).then(resp => resp.json())
      .then(data => {
        algostake_price = data.rate.toFixed(6)
        
      })
}


// get defly price
const getDeflyPrice = async () => {
    await fetch("https://api.livecoinwatch.com/coins/single", {
        method: "POST",
        headers: {
          "content-type": "application/json",
          "x-api-key": process.env.API_KEY,
        },
        body: JSON.stringify({
          currency: "USD",
          code: "DEFLY",
          meta: true,
        }),
      }).then(resp => resp.json())
      .then(data => {
        defly_price = data.rate.toFixed(6)
        
      })
}

//get tinychart price

const getTinyChartPrice = async () => {
  await fetch("https://api.livecoinwatch.com/coins/single", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "x-api-key": process.env.API_KEY,
      },
      body: JSON.stringify({
        currency: "USD",
        code: "TINY",
        meta: true,
      }),
    }).then(resp => resp.json())
    .then(data => {
      tiny_price = data.rate.toFixed(6)
      
    })
}




client.once('ready', () => {
    console.log("Choice Coin V2 Bot 🤖 is ready ")
});

client.on('messageCreate', async (msg) => {
   
    if(msg.guildId === serverID) {
        if( msg.channelId === liquidityChannelID || msg.channelId === priceUpdateChannelID || msg.channelId === algoStakeChannelID || msg.channelId === distributionChannelID || msg.channelId === rewardChannelID) {
            if(msg.content.toLowerCase() === '!about' || msg.content.toLowerCase() === '!about_choice') {           
                 await  msg.reply('Choice Coin is an Algorand Standard Asset that powers Decentralized Decisions, a voting and governance software built directly on the Algorand Blockchain, for more infomation check https://choice-coin.com/')    
             }
             if(msg.content.toLowerCase() === '!yieldly' || msg.content.toLowerCase() === '!yieldly_price') {           
                await getYieldlyPrice()
                await  msg.reply(`Hi 👋🏻 , Yieldly Price is : $${yieldly_price}`)    
            }
            if(msg.content.toLowerCase() === '!defly' || msg.content.toLowerCase() === '!defly_price') {           
                await getDeflyPrice()
                await  msg.reply(`Hi 👋🏻 , Defly Price is : $${defly_price}`)    
            }
            if(msg.content.toLowerCase() === '!algostake' || msg.content.toLowerCase() === '!algostake_price') {           
                await getSTKEPrice()
                await  msg.reply(`Hi 👋🏻 , AlgoStake Price is : $${algostake_price}`)    
            }
             if(msg.content.toLowerCase() === '!github' || msg.content.toLowerCase() === 'github') {           
                await  msg.reply('Here you go 🤌🏽, This is Choice Coin Github URL - https://github.com/ChoiceCoin. Take a look at the repositories, contributions are welcome')    
            }
           if(msg.content.toLowerCase() === '!choice_price' || msg.content.toLowerCase() === '!choice') {           
              await getChoicePrice() 
               await  msg.reply(`Hi 👋🏻 , Choice Coin Price is : $${choice_price}`)    
           }
           
           if(msg.content.toLowerCase() === '!tiny_price' || msg.content.toLowerCase() === '!tiny') {           
              await getTinyChartPrice()
             await  msg.reply(`Hi 👋🏻 , Tiny Chart Price is : $${tiny_price}`)    
         }
         if(msg.content.toLowerCase() === '!algo_price' || msg.content.toLowerCase() === '!algo') {           
          await getAlgoPrice()
         await  msg.reply(`Hi 👋🏻 , Algo Price is : $${algo_price}`)    
     }
           if(msg.content.toLowerCase() === '!choice_market_cap' || msg.content.toLowerCase() === '!market_cap') {
            await getChoicePrice() 
            await  msg.reply(`Hi 👋🏻 , Choice Coin Market Cap is : $${choice_market_cap}`) 
           }
        }
    }
    })


 
const keepAlive = () => {
    app.listen(port, () => {
        console.log(` Choice Coin V2 Bot 🤖 is listening on port ${port}`)
    })
   }

keepAlive()


client.login(process.env.LOGIN_TOKEN);
