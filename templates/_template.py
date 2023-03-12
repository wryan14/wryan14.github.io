TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="style2.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>{heading}</h1>
        </header>

        <main>
            <div class="row">
                <div class="col-md-4">
                    <img src="{image_src}" alt="{image_alt}" class="img-fluid img-cover" style="max-width: 40%;">
                </div>
                <div class="col-md-8">
                    <p><i>"{quote}"</i></p>

                    <p class="lead">Hymn Title: "{hymn_title}"</p>

                    <br>

                    <p>{main_content}</p>
                </div>
            </div>
        </main>
        <section class="bg-light">
            <div class="container">
                <h2>Related Articles</h2>
                <ul class="list-group list-group-flush">
                <li class="list-group-item"><a href="{article_1_url}">{article_1_title}</a></li>
                <li class="list-group-item"><a href="{article_2_url}">{article_2_title}</a></li>
                <li class="list-group-item"><a href="{article_3_url}">{article_3_title}</a></li>
                </ul>
            </div>
        </section>
    </div>

    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5W/ZIjJwZxcfEotg1FfRI8lvL1E6PTjz2lqbSlBfO" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI4+0BpB7DUXhFZeSTP" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min"></script>
</body>
</html>
"""