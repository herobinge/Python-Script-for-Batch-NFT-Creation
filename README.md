# Python-Script-for-Batch-NFT-Creation
作为一位毫无代码经验的设计师，我非常激动地与大家分享一个为大家方便批量生产 NFT 而编写的 Python 脚本。这个脚本利用了 chtgpt 的强大功能，帮助我轻松 批量生成 NFT，我希望这个脚本也能对大家有所帮助。无论你是有经验的开发者还是初学者，这个脚本都能让你简单地创建出大量精美的 NFT。

这是一个批量生成NFT  的脚本，这个脚本的目的是通过随机选择不同的图像部件来生成多个独特的NFT图像。它从预定义的图像部件中选择背景、身体、眼睛、嘴巴和帽子，并将它们组合在一起形成一个新的图像。每个部件有多个可选项，例如不同的背景、眼睛或嘴巴图像，通过随机选择它们来生成不同组合的NFT图像。

脚本使用Pillow库（也称为PIL）来处理图像。它打开每个部件的图像文件，然后将它们叠加在一起形成最终的NFT图像。生成的图像以PNG格式保存在名为imagenft的文件夹中，并根据每个NFT的编号进行命名。

通过调整图像部件的选项和权重，你可以控制生成的NFT图像的多样性和随机性。这个脚本可以用于生成虚拟艺术品集合、游戏角色、个性化头像等等。希望这能帮助你理解脚本的用途。如有其他疑问，请随时提问。

运行上述脚本需要满足以下条件：
1. Python环境：你需要在你的计算机上安装Python解释器。建议使用Python 3.x版本，因为脚本是使用Python 3语法编写的。
2. Pillow库：脚本使用Pillow库来处理图像。你需要安装Pillow库，它是Python的一个图像处理库，提供了对图像的打开、编辑和保存等功能。你可以使用pip工具在命令行中运行以下命令来安装Pillow库：
`pip install pillow`

图像部件文件夹：脚本假设图像部件（背景、眼睛、嘴巴、身体等）被放置在指定的文件夹中。你需要按照脚本中定义的文件夹路径和文件名列表的结构，在桌面（或其他位置）创建相应的文件夹，并将图像部件文件放置在正确的子文件夹中。

确保满足以上条件后，你可以通过运行Python脚本来生成NFT图像。在命令行中切换到脚本所在的目录，并执行以下命令：
`python3 generate_nft.py`
这将运行脚本并生成NFT图像。生成的图像将保存在名为imagenft（你需要在您的桌面创建该文件夹）的文件夹中。
