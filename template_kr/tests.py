# -*- coding: utf-8 -*-
from django.test import TestCase

# Create your tests here.

class TemplateKoreanTestCase(TestCase):
    def setup(self):
        pass

    def test_basic(self):
        self.assertEqual(1,1)

    def test_korean_proofread(self):
        import korean
        result = korean.l10n.proofread("홍수린(는)은 사람이다.")
        self.assertEqual(result, "홍수린은 사람이다.")

    def test_korean_proofread_fail(self):
        import korean
        result = korean.l10n.proofread("홍수린(는)은 사람이다.")

    def test_korean_proofread_tag(self):
        from django.template import Context, Template
        rendered = Template(
            '{% load proofread %}'
            '{{ string|proofread }}'
        ).render(Context({
            'string': '홍수린은(는) 사람이다'
        }))
        self.assertEqual(rendered, '홍수린은 사람이다')
