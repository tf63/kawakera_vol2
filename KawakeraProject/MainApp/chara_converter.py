from chat import Chatgpt

dictionary_character = {
    "gyaru": "受け取った文章をギャルの口調に直してください",
    "ojisan": "受け取った文章を気持ち悪いおじさんの口調に直してください",
}


def character_create(chara="normal"):
    system_setting = dictionary_character[chara]
    chatgpt = Chatgpt(system_setting)
    return chatgpt


def character_converter(dictionary, chara):
    if chara == "normal":
        return dictionary

    else:
        chatgpt = character_create(chara)
        for key in dictionary:
            chatgpt.input_message(dictionary[key])
            dictionary[key] = chatgpt.input_list[-1]["content"]
        return dictionary


if __name__ == "__main__":
    output = character_converter(
        {
            "name": "ダルメシアン",
            "food": "ダルメシアンは犬の一種で、他の犬と同様、肉も野菜も食べる雑食性です。ダルメシアンの健康的な食事は、健康維持に必要な栄養素をすべて含んだ高品質のドッグフードを中心に構成されています。また、ビタミンや食物繊維を摂取するために、ニンジン、インゲン、リンゴなどの野菜や果物も必要です。ダルメシアンは尿路疾患にかかりやすいので、プリン体の少ない食事を与えることが重要です。そのため、ダルメシアンには、レバーや腎臓、一部の魚など、プリン体を多く含む食品を与えないようにする必要があります。",
            "area": "ダルメシアンは家庭犬の一種であり、ペットとして世界中に生息しています。しかし、この犬種の原産地は、かつてユーゴスラビアに属していたクロアチアであり、ダルマチアという地域の名前に由来しています。もともとは馬車と一緒に走る馬車犬として、また番犬として活躍していた犬種です。現在、ダルメシアンは人気のペットで、特徴的な斑点のある被毛とフレンドリーで元気な性格で知られています。",
            "mame": "もちろん！ダルメシアンにまつわる面白いトリビアをご紹介します：\n\n1.ダルメシアンは生まれつき斑点がなく、斑点は通常生後数週間以内に現れます。\n\n2.ダルメシアンは持久力に優れ、長距離を走っても疲れないことで知られています。元々は馬が引く消防車と並んで走るために飼育された。\n\n3.ダルメシアンは強い捕食欲を持ち、リスやウサギなどの小動物を追いかけるのが大好きです。そのため、公共の場や柵のない場所では、リードをつけることが大切です。\n\n4.ダルメシアンは、歴史上、馬車犬、消防署犬、サーカス犬として使われてきました。\n\n5.ダルメシアンは泳ぎが得意で、水遊びを楽しむことができます。もともとはボートで働くために飼育され、現在でも水難救助犬として活躍しています。\n\n6.ダルメシアンは、尿路系が特殊であるため、尿石ができやすいと言われています。そのため、健康上の問題を予防するために、水分補給とプリン体の少ない食事を与えることが大切です。\n\n7.ダルメシアンは、ピンク色の斑点状の皮膚を持つ数少ない犬種のひとつです。",
        },
        "ojisan",
    )
    print(output)
