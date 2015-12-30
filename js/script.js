


var c1 = document.getElementById("canvas1");
var c1_context = c1.getContext("2d");

c1_context.rect(0,0,400,400);
c1_context.fillStyle="black";
c1_context.fill();

$('#canvas1').mousedown(function(e){

  var mouseX = e.pageX - this.offsetLeft;
  var mouseY = e.pageY - this.offsetTop;
		
  paint = true;
  addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
  redraw();
});

$('#canvas1').mousemove(function(e){
  if(paint){
    addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, true);
    redraw();
  }
});

$('#canvas1').mouseup(function(e){
  paint = false;
});

$('#canvas1').mouseleave(function(e){
  paint = false;
});

function resetDrawing(){
	clickX = [];
	clickY = [];
	clickDrag = [];
	var c1 = document.getElementById("canvas1");
	var c1_context = c1.getContext("2d");
	c1_context.rect(0,0,400,400);
	c1_context.fillStyle="black";
	c1_context.fill();
}

function submitDrawing(){
	var canv = document.getElementById("canvas1");
	var image = canv.toDataURL("image/png");
}

var clickX = new Array();
var clickY = new Array();
var clickDrag = new Array();
var paint;

function addClick(x, y, dragging)
{
  clickX.push(x);
  clickY.push(y);
  clickDrag.push(dragging);
}

function redraw(){
	c1_context.clearRect(0, 0, c1_context.canvas.width, c1_context.canvas.height); // Clears the canvas
  
	c1_context.rect(0,0,400,400);
	c1_context.fillStyle="black";
	c1_context.fill();

  	c1_context.strokeStyle = "#FFFFFF";
  	c1_context.lineJoin = "round";
  	c1_context.lineWidth = 20;
			
	for(var i=0; i < clickX.length; i++) {		
    	c1_context.beginPath();
    	if(clickDrag[i] && i){
      		c1_context.moveTo(clickX[i-1], clickY[i-1]);
     	}else{
    c1_context.moveTo(clickX[i]-1, clickY[i]);
    }
    c1_context.lineTo(clickX[i], clickY[i]);
    c1_context.closePath();
    c1_context.stroke();
  }
}
