//
//  ViewController.swift
//  MusicPlayer
//
//  Created by 김혁준 on 2020/02/21.
//  Copyright © 2020 mandarin. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    
    // MARK: IBOutlets
    @IBOutlet var playPauseButton: UIButton!
    @IBOutlet var timeLabel:UILabel!
    @IBOutlet var progressSlder:UISlider!

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func touchUpPlayPauseButton(_ sender:UIButton) {
        print("button tapped")
    }

    @IBAction func sliderValueChanged(_ sender: UISlider) {
        print("slider value changed")
    }
}

