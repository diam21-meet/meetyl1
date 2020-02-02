function btn1() {
			var text=document.createElement("P");
			text.innerHTML="The hospital is cramped and nurse's were rushing around hysterically. A nurse comes up to me and asks me if I need help. I nodded and showed her my purple arms. A gasp escaped her lips as she rushed me to a room. 'How long has this been happening?' 'About a week.' The nurse looked at my hands and shook her head. 'I'm not sure what this is...' she said looking at my arms, 'but this should help.' She handed me a bottle of white ointment";
			assignidfortext.id="hospital"
			document.body.replaceChild(text, ogtext);
			var btn1 = document.getElementById("button1"); 
			var new_button=document.getElementById("button3");
			make_style_appear.style.display="block";
			replacenbtn_w_ogbtn.parentNode.replaceChild(btn3, hospitalbtn);
			var btn2=document.getElementById("button2");
			var btn4=document.getElementById("button4");
			btn4.style.display="block";
			btn2.parentNode.replaceChild(btn4, btn2);
		}