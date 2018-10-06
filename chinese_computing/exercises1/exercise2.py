import i18n

i18n.add_translation('money', {
    'zero': 'You do not have any money!',
    'one': 'You only have %{count} dollar...',
    'few': 'You just have %{count} dollars.',
    'many': 'God! You have %{count} dollars!!!'
})
print(i18n.t('money', count=0))
print(i18n.t('money', count=1))
print(i18n.t('money', count=5))
print(i18n.t('money', count=10000000))


#
# i18n.set("file_format", "json")
# i18n.load_path.append(".")
#
# i18n.set("locale", "fr")
# print(i18n.t("languages.inquiry"))
#
# i18n.set("locale", "en")
# print(i18n.t("languages.inquiry"))
#
# i18n.set("locale", "cn")
# print(i18n.t("languages.inquiry"))



