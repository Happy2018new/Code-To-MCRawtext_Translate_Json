{
    "结构体": # 结构体(数量不作限制，可以超过传统的 8 个)
    [
        {
            "分数条件":
            {
                "\"Happy2018new\"": # 这里的 Happy2018new 是计分板，不一定必须加引号，按需要就可
                [
                    [8,12]
                ],
                "DEMO1": # 这里的 DEMO1 是计分板
                [
                    [1,2],
                    [7,9]
                ]
            },
            # 当 @s 在 Happy2018new 的分数为 8..12 且在 DEMO1 的分数为 1..2 或 7..9 时依次显示 内容 中的所有元素
            # 如果 内容 内有嵌套，则根据 嵌套 内提供的 分数条件 决定对应的内容是否显示
            "嵌套位置":[2,3], # 在 内容 的第二项和第三项嵌套一个 {"计分板名称":"","结构体":[]}
            "内容":
            [
                {"text":"不好"}, # 第一项内容
                {
                    "结构体": # 同第 3 行注释
                    [
                        {
                            "分数条件":
                            {
                                "abcd": # 这里的 abcd 是计分板
                                [
                                    ["min","max"]
                                ]
                            },
                            # 当 @s[scores={abcd=-2147483648..2147483647}] 可以选中时依次显示 内容 中的所有元素
                            # 如果 内容 内有嵌套，则根据 嵌套 内提供的 分数条件 决定对应的内容是否显示
                            "嵌套位置":[],
                            # 这里列表是空的，说明 内容 里面没有要嵌套 {"计分板名称":"","结构体":[]} 的元素
                            "内容":
                            [
                                {"score":{"objective":"√","name":"*"}},
                                {"text":"测试"}
                                # 众所周知，你可能需要显示很多个东西，所以你可以发现这个
                                # “内容”是个列表
                            ]
                        }
                    ]
                },
                {
                    "结构体": # 同第 3 行注释
                    [
                        {
                            "分数条件":
                            {
                                "\"123\"": # 这里的计分板名称是 123 ，而且必须加引号了
                                [
                                    ["Min",-2018],
                                    [16,"Max"]
                                ]
                            },
                            # 当 @s[scores={Happy2018new=..-233}] 或 @s[scores={Happy2018new=16..}]
                            # 可以选中时依次显示 内容 中的所有元素
                            # 如果 内容 内有嵌套，则根据 嵌套 内提供的 分数条件 决定对应的内容是否显示
                            "嵌套位置":[],
                            # 这里列表是空的，说明 内容 里面没有要嵌套 {"计分板名称":"","结构体":[]} 的元素
                            "内容":
                            [
                                # 空的不会显示任何东西
                                # 但由于一个奇怪的特性，最终会添加一个 {"text":""} 充当占位符
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}

# 文件名字应该是 input.json ，用 .py 作为后缀名只是为了方便注释
# 你可以无限嵌套下去。我并没有在代码中限制递归深度。但是 python 自己有默认的递归深度，也就是 1000
# 不过，递归 1000 次的话，可能命令方块都塞不下指令吧
# 除非，你是禽兽？？