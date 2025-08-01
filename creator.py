def create_html_file(date_english,
                     date_hebrew,
                     parsha_english,
                     parsha_hebrew,
                     latest_candle_lighting,
                     earliest_candle_lighting,
                     sunset_kabbalat_shabbat,
                     latest_shema,
                     mincha_shabbat,
                     havdala,
                     shabbat_shacharit_times,
                     sunset_mincha_chol,
                     plag_mincha_chol,
                     late_maariv_times=[],
                     filename="index.html",
                     logo_url="Logo/grey logo transparent.png",
                     plag_kabbalat_shabbat="N/A"):
    """
    Creates an HTML file containing the provided code string.

    Args:
        code_string (str): The code to be embedded in the HTML file.
        filename (str, optional): The name of the HTML file to create. Defaults to "index.html".
    
    """
    if not len(late_maariv_times) == 1:
        late_maariv_times = " PM, ".join(late_maariv_times) + " PM"
    else:
      late_maariv_times = late_maariv_times[0]
    shabbat_shacharit_times = "AM, ".join(shabbat_shacharit_times) + " AM"
    print(len(parsha_english))
    font_size = '3.0rem'
    if len(parsha_english) +8  > 25:
      font_size = '2.6rem'
    if len(parsha_english) + 8 > 35:
      font_size = '2.2rem'
    html_content = """
    <!DOCTYPE html>
    <head>
      <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap" rel="stylesheet">
    <style>
    * {
      margin:0;
      padding:0;
      box-sizing:border-box;
    }
    @page {
    size: 8.5cm 10.5cm;
    margin: 0;
    }
    html {
      font-size:31.5%;
    }
    body {
      height:100vh;
      display:flex;
      justify-content:center;
      align-items:center;
      font-family:"Open Sans", sans-serif;

    }
    .box, .card {
      border: 2px solid black;

    }
    .box{
      position:relative;
    }
    .card {
      width:8.5cm;
      height:10.5cm;
    }

    .content {
      padding:10px 25px;
    }
    .logo {
    position: absolute;
    opacity: 75%;
    width: 40px;
    right: 5px;
    top: 2px;
   }
    .disclaimer {
       position: absolute;
    transform: rotate(270deg) translateY(-50%);
    top: 76%;
    right: -77px;
    font-family: 'Open Sans';
    font-weight: 700;
    font-size: 1.0rem;
    }
    .header {
      text-align:center;
      margin-bottom:6px;
      """ + f"""
      font-size:{font_size};
      """ + """
   

    }
    .date {
      margin-bottom:5px;
      text-align:center;
      font-size:2.2rem;
      font-weight:500;
    }
    .candle-lighting {
      text-align:center;
      font-size:3.0rem;
      margin-top:5px;

    }
    .line {
      width:100%;
          background-color:black;
          height:1px;

    }
    .head-line-container {
      display:flex;
      justify-content:center;
    }
    .date-line {
        margin: 0 20px;

    }
    .latest {
      display:block;
      text-align:center;
      font-weight:700;
      font-size:12.0rem;
      margin-top:-13px;
    }
    .earliest {
      font-weight:750;;
      display:block;
      text-align:center;
      margin-top:-6px;
      font-size:1.4rem;
    }
    .erev-shabbos {
      margin-top:8px;
    }
    .shabbos-title {
      font-size:1.8rem;
    }
    .davening-time {
      font-size:1.5rem;
      display:block;

    }
    .bold {
      font-weight:750;
    }
    .shabbos-day {
      margin-top:8px;
      margin-bottom:3px;
    }

    .line-container {
      display:grid;
      grid-template-columns: 1fr auto 1fr;
      justify-items:center;
      align-items:center;
      column-gap:15px;


    }


    .upcoming-title {
      font-size:1.8rem;
    }
    .weekday-minyanim {
      margin-top: -6px;
      padding:5px;
      border: 1px solid black;
      border-top: none;

    }

    .slight-margin-left {
      margin-right:5px;
      margin-bottom:10px;
    }
    .slight-margin-bottom {
      margin-bottom:10px;

    }

    </style>
    </head>
    """ + f"""
    <body class="container">
    <main class="box card">
      <div class="content">
        <img class="logo"src="{logo_url}" alt="BAYT LOGO"/>
        <span class="disclaimer">*All times are subject to change - Please refer to weekly bulletin
      </span>
        <h2 class="header"> Parshas {parsha_english} </h2>
      <h2 class ="header"> {'פרשת'} {parsha_hebrew} <h2>
        <h3 class="date"> {date_english} | {date_hebrew} </h3>
        <div class="head-line-container">
        <div class="line date-line">&nbsp; </div>
        </div>
          <h3 class= "candle-lighting">
            Candle Lighting | הדלקת נרות
          </h3>
          <span class="latest"> {latest_candle_lighting} </span>
        {f'''<span class="earliest"> Earliest Candle Lighting | {earliest_candle_lighting} PM </span> ''' if earliest_candle_lighting else ''}
        <div class="erev-shabbos">
            <h6 class="shabbos-title"> Erev Shabbos</h6>
              {f'''  <span class="davening-time"> Plag Mincha & Kabbalas Shabbos | <span class="bold"> {plag_kabbalat_shabbat} PM </span></span>'''if plag_kabbalat_shabbat else ''}
                  <span class="davening-time"> Mincha & Kabbalas Shabbos | <span class="bold"> {sunset_kabbalat_shabbat} PM </span>
                </span> 
                  </div>
        <div class="shabbos-day">
            <h6 class="shabbos-title">Shabbos Day</h6>
                <span class="davening-time"> Shacharis | <span class="bold"> {shabbat_shacharit_times} </span></span>
              <span class="davening-time"> Latest Shema | <span class="bold"> {latest_shema} AM </span>
                </span> 
          <span class="davening-time"> Mincha | <span class="bold"> {mincha_shabbat} PM </span>
                </span> 
          <span class="davening-time"> Havdalah | <span class="bold"> {havdala} PM </span>
                </span> 
                  </div>
        <div class "upcoming">
          <div class="line-container">
            <div class="line upcoming-line">&nbsp;</div>
            <h4 class="upcoming-title"> Upcoming Weekday Davening </h4>
                    <div class="line upcoming-line">&nbsp;</div>

          </div>
          <div class="weekday-minyanim">
            <h6 class="davening-time bold"> Shacharis </h6>
            <span class="davening-time"> Sun | <span class="bold"> 6:45 AM 8:00 AM 9:00 AM </span></span>
            <span class="davening-time"> Mon & Thurs | <span class="bold slight-margin-left"> 6:20 AM </span> Tues, Wed & Fri | <span class="bold"> 6:30 AM </span></span>
            <span class="davening-time slight-margin-bottom"> Mon - Fri | <span class="bold "> 6:45 AM 8:00 AM 9:00 AM </span></span>
               {f'''<span class="davening-time"> Plag Mincha/Maariv | <span class="bold"> {plag_mincha_chol} PM </span>
                </span>''' if plag_mincha_chol  else '' }
               <span class="davening-time"> Mincha/Maariv | <span class="bold"> {sunset_mincha_chol} PM </span>
                </span> 
               <span class="davening-time"> Late Maariv | <span class="bold"> {late_maariv_times} </span>
                </span> 
          </div>
        </div>
        </div>



        </main>
      </body>

    """

    with open(f"./HTML/{filename}", "w") as f:
        f.write(html_content)

    print("index.html file created successfully.")
