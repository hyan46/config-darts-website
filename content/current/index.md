---
title: Current
date: 2022-10-24

type: landing

sections:
  - block: markdown
    content:
      title: Our current work
      subtitle: Identify HIV clusters using real time, streaming case-report data from the WA DOH.
      text: |
        - Rapidly identify spatial/temporal clusters from individuals who seek health care. 
        - We will use case report rather than phylogenetics to significantly reduce the time to identifying clusters and obtain significantly fewer missing cases but will lose the transmission chain. 
        - Therefore, we aim to combine our approach with transmission/phylogeny whenever available. 
        - Rigorous assessment and comparison is major part of the ongoing research.


---
<link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
<script defer src="https://pyscript.net/latest/pyscript.js"></script>
<py-config>
    plugins = [
      "https://pyscript.net/latest/plugins/python/py_tutor.py"
    ]
</py-config>

<section class="pyscript">
    Hello world! <br>
    This is the current date and time, as computed by Python:
    <py-script>
        from datetime import datetime
        now = datetime.now()
        display(now.strftime("%m/%d/%Y, %H:%M:%S"))
    </py-script>
</section>
<!-- <div id="demo">
  <h2>Let AJAX change this text</h2>
  <button type="button" onclick="loadPY()">Change Content</button>
  <iframe src="/public/yearggg2021.html" width="100%" height="120"></iframe>
</div> -->

<script>
//   $.ajax({
//    url: "/path/to/your/script",
//    success: function(response) {
//      // here you do whatever you want with the response variable
//    }
// });
// function loadPY() {
//   $.ajax({
//     url: "/path/to/your/script",
//     success: loadPY(response) {
//       document.getElementById("demo").innerHTML = this.responseText;
//     }
//  });
// }
</script>