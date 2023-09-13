---
title: Methods
date: 2022-10-24

type: landing

sections:
  - block: hero
    content:
      title: |
        Methods for Detecting Anomalies in Real-Time Survelliance
      image:
        filename: TST_Data.png
      text: |
        <br>
        
        Tensor Spatial-temporal Data Decomposition Method
  - block: markdown
    content:
      title: Our approach adapts to many different settings and diseases
      text: |
        - Multi-drug resistant gonorrhea 
        - HIV
        - Monkey pox
        - Covid 
        - Syphilis in women

        - Major crime occurrences
        - Tainted drug overdose, Fentanyl overdoes deaths is a major public health problem in Seattle.  Currently contacting Seattle/King County Public Health to obtain data. 
  
  - block: markdown
    content:
      text: |
        
        <html><div>Hello World!</div></html>
        <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
        <script defer src="https://pyscript.net/latest/pyscript.js"></script>
        

            <section class="pyscript">
              <py-config>
                    plugins = [
                      "https://pyscript.net/latest/plugins/python/py_tutor.py"
                    ]
              </py-config>
              <py-config>
                  [[fetch]]
                  files = ["./plt_hello.py"]
              </py-config>
                Hello world! <br>
                This is the current date and time, as computed by Python
                <py-script>
                    from datetime import datetime
                    now = datetime.now()
                    display(now.strftime("%m/%d/%Y, %H:%M:%S"))
                </py-script>
                <py-script src="./plt_hello.py">
                
                </py-Script>
            </section>

---

