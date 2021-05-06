//
//  ViewController.swift
//  Dicee-iOS13
//
//  Created by Angela Yu on 11/06/2019.
//  Copyright © 2019 London App Brewery. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var dice1: UIImageView!
    @IBOutlet weak var dice2: UIImageView!
    

    @IBAction func rollPressed(_ sender: UIButton) {
        //print("Button got tapped.")
        let diceArray = [#imageLiteral(resourceName: "DiceOne"),#imageLiteral(resourceName: "DiceTwo"),#imageLiteral(resourceName: "DiceThree"),#imageLiteral(resourceName: "DiceFour"),#imageLiteral(resourceName: "DiceFive"),#imageLiteral(resourceName: "DiceSix")]
        //dice1.image = diceArray[Int.random(in: 0...5)]
        //dice1.image = diceArray[Int.random(in: 0...<6)]
        //Float.random(in: 0...5)
        //Boolean.random()
        //array.shuffle()
        dice1.image = diceArray.randomElement()
        dice2.image = diceArray.randomElement()
    }
    
}

