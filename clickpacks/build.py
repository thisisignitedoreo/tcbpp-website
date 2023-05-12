import json

data = json.load(open("clickpack_index.json"))

html = """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>tcb++ clickpack index</title>
	<style>
		@import url("https://raw.githubusercontent.com/source-foundry/Hack/master/build/web/hack.css");
		* {
			color: white;
			font-family: "hack", monospace;
			padding: 5px;
			margin-top: 0;
			margin-bottom: 0;
		}
		html {
			background-color: #FF7700;
		}
		.grid {
			display: grid;
			grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
			column-gap: 10px;
			row-gap: 10px;
		}
		.grid-item {
			border: solid #FF9900;
			border-radius: 15px;
			background-color: #FF8500;
		}
	</style>
</head>
<body>
	<div style="text-align: center">
		<h1>tcb++ clickpack index</h1>
		<div class="grid">"""

for k, i in enumerate(data):
	html += f"""
			<div class="grid-item">
				<h3>{i["title"]}<br>
				by: {i["author"]}</h3>
				<h4>{i["description"]}</h4>
				<a href="javascript:void" onclick="play(0)">Test</a>
				<a href="/clickpacks/{k}/clickpack.zip">Download</a>
			</div>"""

html += """
		</div>
	</div>
	<script type="text/javascript">
		function choose(choices) {
			var index = Math.floor(Math.random() * choices.length);
			return choices[index];
		}
		function play(index) {
			fetch(`/clickpacks/$\{index\}/data.json`)
				.then((response) => response.json())
				.then((data) => {
					var hold = new Audio(`/clickpacks/$\{index\}/holds/${choose(data.holds)}`)
					var release = new Audio(`/clickpacks/$\{index\}/releases/${choose(data.releases)}`)
					hold.play()
					release.play()
				});
		}
	</script>
</body>
</html>"""

open("index.html", "w").write(html)

