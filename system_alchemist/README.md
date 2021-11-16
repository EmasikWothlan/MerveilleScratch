# Potion and Content

这里试着对药剂类进行初步的试验。

希望在这个试验稿中能够探索出一条道路用来描述具有下述特点的药水：

- 标签自定义的药水。
- 可以进行多次拆分的药水。
    - 比如 100mL 的药水可以被分成十个 10mL 的药水。
- 可以被随意合并的药水。
    - 比如将 10mL 药水A 和 10mL 药水B 倒在一起成为 20mL 药水混合物。
- 药水中可以添加自定义的溶剂。
    - 在拆分药水时，药水中的溶剂成分也会相应被分成两份。
- 根据调和人的技术，可以花费额外的资源使得药水的成分难以被识别。
- 根据调和人的技术，可以花费额外的资源使得药水中的特定成分难以被识别。

## 成分识别

对于识别成分问题，目前的设计如下：

- 所有人都可以进行非常简单的鉴别，比如看颜色，看形态之类。
- 从某个层面开始，鉴别难度就提高了，需要借助到工具了。
- 再从某个层面开始，难度会提高到需要高级鉴别技能的角色才能识别了。

### 实现思路

使用元类动态生成新的类并以 `TypeName(amount)` 为参数进行实例化。

常人可以通过检查由类名直接生成的外观描述 `.describe()`来判断药物是否是真的。

但只有专业人士才能用 `.test()` 方法来判断药物是否掺假或者被隐秘地下毒。
