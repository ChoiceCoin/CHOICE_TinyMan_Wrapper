import fetch from 'node-fetch';
import { Client, Intents } from 'discord.js';
import express from 'express';

const app = express();

const port = process.env.PORT || 3000;

import dotenv from 'dotenv'
 dotenv.config();

const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

const serverID = '859233439168069682';
const priceUpdateChannelID = '945403182413127690';
const liquidityChannelID = '907444405831598110';



let choice_price;
let choice_market_cap;

let algo_price

app.get('/', (req,res) => {
    res.json('Choice Coin V2 Bot 🤖 is up and running')
})

// getting choice price from liveCoinWatch API
const getChoicePrice =  () => {
 fetch("https://api.livecoinwatch.com/coins/single", {
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
        choice_price = data.rate.toFixed(8)
        choice_market_cap = data.cap
        
      })
      
}

getChoicePrice() 

//getting algo price from LiveCoinWatch API
const getAlgoPrice = () => {
    fetch("https://api.livecoinwatch.com/coins/single", {
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

getAlgoPrice()



client.once('ready', () => {
    console.log("Choice Coin V2 Bot 🤖 is ready ")
});

client.on('messageCreate', async (msg) => {
   
    if(msg.guildId === serverID) {
        if( msg.channelId === liquidityChannelID || msg.channelId === priceUpdateChannelID) {
            if(msg.content.toLowerCase() === '!about' || msg.content.toLowerCase() === '!about_choice') {           
                 await  msg.reply('Choice Coin is an Algorand Standard Asset that powers Decentralized Decisions, a voting and governance software built directly on the Algorand Blockchain, for more infomation check https://choice-coin.com/')    
             }
             if(msg.content.toLowerCase() === '!github' || msg.content.toLowerCase() === 'github') {           
                await  msg.reply('Here you go 🤌🏽, This is Choice Coin Github URL - https://github.com/ChoiceCoin. Take a look at the repositories, contributions are welcome')    
            }
           if(msg.content.toLowerCase() === '!choice_price' || msg.content.toLowerCase() === '!choice') {           
              getChoicePrice() 
               await  msg.reply(`Hi 👋🏻 , Choice Coin Price is : $${choice_price}`)    
           }
           if(msg.content.toLowerCase() === '!algo_price' || msg.content.toLowerCase() === '!algo') {           
            getChoicePrice() 
             await  msg.reply(`Hi 👋🏻 , Algo Price is : $${algo_price}`)    
         }
           if(msg.content.toLowerCase() === '!choice_market_cap' || msg.content.toLowerCase() === '!market_cap') {
            getChoicePrice() 
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